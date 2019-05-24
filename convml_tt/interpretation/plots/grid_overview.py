import math

import matplotlib.pyplot as plt
import numpy as np

from ... import TileType


def grid_overview(triplets, points, tile=TileType.ANCHOR,
                  figwidth=16, ncols=10, include_number=True):
    """
    Plot a grid overview of the chosen tile at the selected `points`. If
    `points` is an integer the first N=points tiles will be plotted, if
    `points` is a list it will be interpreted as indecies into `triplets`
    """

    if isinstance(points, int):
        idxs = np.arange(points)
    elif isinstance(points, np.ndarray):
        idxs = points
    elif isinstance(points, list):
        idxs = np.array(points)
    else:
        raise NotImplementedError(type(points))

    nrows = math.ceil(float(len(idxs))/float(ncols))
    figheight = float(figwidth)/ncols*nrows
    figsize = (figwidth, figheight)

    lspace = 0.05
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize,
                             gridspec_kw=dict(hspace=lspace, wspace=lspace))

    for n, i in enumerate(idxs):
        ax = axes.flatten()[n]
        ax.axison = False
        tile = triplets[i][0]
        tile.show(ax=ax)
        ax.set_aspect('equal')
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        if include_number:
            ax.text(0.1, 0.1, i, transform=ax.transAxes,
                    bbox={'facecolor': 'white', 'alpha': 0.4, 'pad': 2})

    for n in range(len(idxs), nrows*ncols):
        ax = axes.flatten()[n]
        ax.axison = False