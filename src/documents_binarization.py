import cv2
import numpy as np
from keras.models import Model
from keras.optimizers import Adam
from keras.layers.merge import concatenate
from keras.layers.normalization import BatchNormalization
from keras.layers.core import SpatialDropout2D, Activation
from keras.layers import Input, Conv2D, MaxPooling2D, UpSampling2D

from config.paths import PATH_TO_WEIGHTS
from src.images_utils import ImagesUtils


class DocumentBinarizer:
    def __init__(self):
        self._img_utils = ImagesUtils()

        self._model = self.__get_model()
        self._model.load_weights(PATH_TO_WEIGHTS)
        self._model.compile(optimizer=Adam(lr=1e-4), loss='binary_crossentropy', metrics=['accuracy'])

    def binarize(self, filename):
        img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE).astype(np.float32)
        img = self._img_utils.binarize_img(img, self._model)

        return img

    @staticmethod
    def __double_conv_layer(inputs, filters):
        """Create stacked conv layers."""

        conv = Conv2D(filters, (3, 3), padding='same', kernel_initializer='he_normal')(inputs)
        conv = BatchNormalization(axis=3)(conv)
        conv = Activation('relu')(conv)
        conv = Conv2D(filters, (3, 3), padding='same', kernel_initializer='he_normal')(conv)
        conv = BatchNormalization(axis=3)(conv)
        conv = Activation('relu')(conv)
        conv = SpatialDropout2D(0.1)(conv)

        return conv

    def __down_layer(self, inputs, filters):
        """Create down-sampling layer."""

        conv = self.__double_conv_layer(inputs, filters)
        pool = MaxPooling2D(pool_size=(2, 2))(conv)

        return conv, pool

    def __up_layer(self, inputs, concats, filters):
        """Create up-sampling layer."""

        return self.__double_conv_layer(concatenate([UpSampling2D(size=(2, 2))(inputs), concats], axis=3), filters)

    def __get_model(self):
        """Create U-net."""

        inputs = Input((128, 128, 1))

        # Down-sampling.
        down1, pool1 = self.__down_layer(inputs, 32)
        down2, pool2 = self.__down_layer(pool1, 64)
        down3, pool3 = self.__down_layer(pool2, 128)
        down4, pool4 = self.__down_layer(pool3, 256)
        down5, pool5 = self.__down_layer(pool4, 512)

        # Bottleneck.
        bottleneck = self.__double_conv_layer(pool5, 1024)

        # Up-sampling.
        up5 = self.__up_layer(bottleneck, down5, 512)
        up4 = self.__up_layer(up5, down4, 256)
        up3 = self.__up_layer(up4, down3, 128)
        up2 = self.__up_layer(up3, down2, 64)
        up1 = self.__up_layer(up2, down1, 32)

        outputs = Conv2D(1, (1, 1))(up1)
        outputs = Activation('sigmoid')(outputs)

        model = Model(inputs, outputs)

        return model
