#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def center(a):
    return tuple((i / 2 - 0.5 for i in a.shape[0:2]))


def radial_distance(a):
    height, weight = a.shape[0], a.shape[1]
    y, x = center(a)
    Y = np.full((weight, height), range(height)).T
    X = np.full((height, weight), range(weight))
    return np.sqrt((Y - y) ** 2 + (X - x) ** 2)


def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
    [tmin,tmax]."""
    return np.interp(a, (a.min(), a.max()), (tmin, tmax))


def radial_mask(a):
    return scale(1 - radial_distance(a))


def radial_fade(a):
    return a * radial_mask(a)[:, :, np.newaxis]


def main():
    image = plt.imread("src/painting.png")
    fig, ax = plt.subplots(3, 1)
    ax[0].imshow(image)
    ax[1].imshow(radial_mask(image))
    ax[2].imshow(radial_fade(image))
    plt.show()


if __name__ == "__main__":
    main()
