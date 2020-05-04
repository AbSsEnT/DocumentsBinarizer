from keras.models import Model
from keras.layers.merge import concatenate
from keras.layers.normalization import BatchNormalization
from keras.layers.core import SpatialDropout2D, Activation
from keras.layers import Input, Conv2D, MaxPooling2D, UpSampling2D


def double_conv_layer(inputs, filters):
    """Create stacked conv layers."""

    conv = Conv2D(filters, (3, 3), padding='same', kernel_initializer='he_normal')(inputs)
    conv = BatchNormalization(axis=3)(conv)
    conv = Activation('relu')(conv)
    conv = Conv2D(filters, (3, 3), padding='same', kernel_initializer='he_normal')(conv)
    conv = BatchNormalization(axis=3)(conv)
    conv = Activation('relu')(conv)
    conv = SpatialDropout2D(0.1)(conv)

    return conv


def down_layer(inputs, filters):
    """Create down-sampling layer."""

    conv = double_conv_layer(inputs, filters)
    pool = MaxPooling2D(pool_size=(2, 2))(conv)

    return conv, pool


def up_layer(inputs, concats, filters):
    """Create up-sampling layer."""

    return double_conv_layer(concatenate([UpSampling2D(size=(2, 2))(inputs), concats], axis=3), filters)


def unet():
    """Create U-net."""

    inputs = Input((128, 128, 1))

    # Down-sampling.
    down1, pool1 = down_layer(inputs, 32)
    down2, pool2 = down_layer(pool1, 64)
    down3, pool3 = down_layer(pool2, 128)
    down4, pool4 = down_layer(pool3, 256)
    down5, pool5 = down_layer(pool4, 512)

    # Bottleneck.
    bottleneck = double_conv_layer(pool5, 1024)

    # Up-sampling.
    up5 = up_layer(bottleneck, down5, 512)
    up4 = up_layer(up5, down4, 256)
    up3 = up_layer(up4, down3, 128)
    up2 = up_layer(up3, down2, 64)
    up1 = up_layer(up2, down1, 32)

    outputs = Conv2D(1, (1, 1))(up1)
    outputs = Activation('sigmoid')(outputs)

    model = Model(inputs, outputs)

    return model
