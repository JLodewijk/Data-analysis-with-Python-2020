#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def to_grayscale(image):
    print(image.shape)
    weights = [0.2126, 0.7152, 0.0722]
    return np.sum(weights * image, axis=2)


def to_red(image):
    # Make image red
    weights = [1, 0, 0]
    return image * weights


def to_green(image):
    # Make image green
    weights = [0, 1, 0]
    return image * weights


def to_blue(image):
    # Make image blue
    weights = [0, 0, 1]
    return image * weights


def main():
    painting = plt.imread("src/painting.png")
    fig, ax = plt.subplots(3, 1)
    ax[0].imshow(to_red(painting))
    ax[1].imshow(to_green(painting))
    ax[2].imshow(to_blue(painting))
    plt.show()

    greyscaled = to_grayscale(painting)
    plt.imshow(greyscaled)
    plt.gray()
    plt.show()


if __name__ == "__main__":
    main()
