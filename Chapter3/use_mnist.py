import sys, os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist
from PIL import Image
import numpy as np


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

(x_train, t_train), (x_test, t_test) = load_mnist(flatten = True, normalize = False)
img = x_train[0]
label = t_train[0]
img = img.reshape(28, 28)
img_show(img)
