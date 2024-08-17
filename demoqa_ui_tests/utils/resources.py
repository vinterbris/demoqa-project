import os

import resources

RES_DIR = os.path.abspath(os.path.join(os.path.dirname(resources.__file__), "images"))


def path(img_name):
    return os.path.join(RES_DIR, img_name)
