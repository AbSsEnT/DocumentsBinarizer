import time

from keras.optimizers import Adam

from src.model import unet
from src.images_utils import *

PATH_TO_INPUTS = os.path.join(".", "inputs")
PATH_TO_OUTPUTS = os.path.join(".", "outputs")
PATH_TO_WEIGHTS = os.path.join(".", "weights", "weights.hdf5")


if __name__ == "__main__":
    start_time = time.time()

    in_filename = "sample_2.png"

    model = unet()
    model.compile(optimizer=Adam(lr=1e-4), loss='binary_crossentropy', metrics=['accuracy'])
    model.load_weights(PATH_TO_WEIGHTS)

    img = cv2.imread(os.path.join(PATH_TO_INPUTS, in_filename), cv2.IMREAD_GRAYSCALE).astype(np.float32)
    img = binarize_img(img, model)
    cv2.imwrite(os.path.join(PATH_TO_OUTPUTS, in_filename), img)

    print("finished in {0:.2f} seconds".format(time.time() - start_time))
