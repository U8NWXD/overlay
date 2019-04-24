#!/usr/bin/env python3

# This file is part of overlay: Makes multi-image composites
# Copyright (c) 2018-2019 U8N WXD (github.com/U8NWXD) <cs.temporary@icloud.com>
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Combine a set of image files into a composite image by averaging pixel values

Usage: overlay.py [mean | median] img1 img2 [additional images]

The number of arguments is validated, but not the arguments themselves. If the
mean is used to average, the composite image is named ``composite_mean.jpg``. If
the median is used, the composite image is named ``composite_median.jpg``.

Any existing composite image with the same name is overwritten.
"""

from PIL import Image
import numpy as np
import sys


def composite_multi(images, use_mean=False):
    """Combine a set of images into a composite by averaging the pixel values

    :param images: Set of images to combine
    :param use_mean: Whether to average using the mean, by default uses median
    :return: Composite image
    """

    # SOURCE: Reti43 on StackOverflow
    # https://stackoverflow.com/a/34625033
    # Original content licensed under CC-BY-SA 4.0 per StackOverflow terms
    # https://creativecommons.org/licenses/by-sa/4.0/
    # This method is a derivative work and available under CC-BY-SA 4.0

    size = images[0].size
    images_array = np.zeros(shape=(len(images), size[1], size[0], 3))

    for i, image in enumerate(images):
        images_array[i] = np.array(image.resize(size))
    if use_mean:
        combined_pixels = np.mean(images_array, axis=0).astype(np.uint8)
    else:
        combined_pixels = np.median(images_array, axis=0).astype(np.uint8)
    image = Image.fromarray(combined_pixels)
    return image


if __name__ == "__main__":
    use_mean = False
    usage = "Usage: overlay.py [mean | median] img1 img2 [additional images]"
    if len(sys.argv) < 3:
        print("ERROR: Insufficient arguments provided.")
        print(usage)
        exit(1)
    if sys.argv[1] == "mean" or sys.argv[1] == "median":
        if len(sys.argv) < 4:
            print("ERROR: Please specify at least 2 files to combine.")
            print(usage)
            exit(1)
        image_paths = sys.argv[2:]
        use_mean = sys.argv[1] == "mean"
    else:
        if len(sys.argv) < 3:
            print("ERROR: Please specify at least 2 files to combine.")
            print(usage)
            exit(1)
        image_paths = sys.argv[1:]

    image_set = [Image.open(path) for path in image_paths]
    composite = composite_multi(image_set, use_mean)
    if use_mean:
        name = "composite_mean.jpg"
    else:
        name = "composite_median.jpg"
    composite.save(name, format="JPEG")
