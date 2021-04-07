#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def subfigures(a):
    figure_plot, axis_plot = plt.subplots(1, 2)
    axis_plot[0].plot(a[:, 0], a[:, 1])
    axis_plot[1].scatter(a[:, 0], a[:, 1], c=a[:, 2], s=a[:, 3])
    plt.show()


def main():
    a = np.column_stack([[1, 2, 3], [2, 4, 6], [0.24, 2.99, -1.49], [25, 50, 10]])
    subfigures(a)


if __name__ == "__main__":
    main()
