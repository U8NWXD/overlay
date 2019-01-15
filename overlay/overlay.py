from PIL import Image
import numpy as np
import sys


def composite_multi(images):

    # SOURCE: Reti43 on StackOverflow
    # https://stackoverflow.com/a/34625033
    # Original content licensed under CC-BY-SA 4.0 per StackOverflow terms
    # https://creativecommons.org/licenses/by-sa/4.0/
    # This method is a derivative work and available under CC-BY-SA 4.0

    size = images[0].size
    images_array = np.zeros(shape=(len(images), size[1], size[0], 3))

    for i, image in enumerate(images):
        images_array[i] = np.array(image.resize(size))
    median_pixels = np.median(images_array, axis=0).astype(np.uint8)
    image = Image.fromarray(median_pixels)
    return image


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("ERROR: Please specify at least 2 files to combine.")
        exit(1)
    images = [Image.open(path) for path in sys.argv[1:]]
    composite = composite_multi(images)
    composite.save("composite.jpg", format="JPEG")
