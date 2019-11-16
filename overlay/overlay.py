#!/usr/bin/env python3

# This file is part of overlay: Makes multi-image composites
# Copyright (c) 2018-2019 U8N WXD (github.com/U8NWXD) <cs.temporary@icloud.com>
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Combine image files into a composite image by averaging pixel values

Usage: overlay.py [mean | median] img1 img2 [additional images]

The number of arguments is validated, but not the arguments themselves.
If the mean is used to average, the composite image is named
``composite_mean.jpg``. If the median is used, the composite image is
named ``composite_median.jpg``.

Any existing composite image with the same name is overwritten.
"""

from typing import List
import sys
import argparse

from PIL import Image
import numpy as np


def composite_multi(images: List["Image"], use_mean: bool = False):
    """Combine a set of images into a composite by averaging the pixel values

    This method was inspired by Reti43 on StackOverflow
    https://stackoverflow.com/a/34625033.

    Arguments:
        images: Set of images to combine
        use_mean: Whether to average using the mean, by default uses median

    Returns:
        Composite image
    """
    width, height = images[0].size
    images_array = np.zeros(shape=(len(images), height, width, 3))

    for i, image in enumerate(images):
        images_array[i] = np.array(image.resize((width, height)))
    combo_func = np.mean if use_mean else np.median
    combined_pixels = combo_func(images_array, axis=0).astype(np.uint8)
    return Image.fromarray(combined_pixels)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="overlay: Makes multi-image composites",
        epilog=(
            "Copyright (c) 2018-2019 U8N WXD (github.com/U8NWXD). "
            "Project, including licensing details, can be found at "
            "https://github.com/U8NWXD/overlay."
        ),
    )
    parser.add_argument(
        "images", nargs="+",
        help="Space-separated paths to the images to combine"
    )
    parser.add_argument(
        "--mean", action="store_true",
        help="Combine pixel values by the mean instead of the median"
    )
    args = parser.parse_args()
    images = [Image.open(path) for path in args.images]
    composite = composite_multi(images, args.mean)
    name = "composite_mean.jpg" if args.mean else "composite_median.jpg"
    composite.save(name, format="JPEG")
