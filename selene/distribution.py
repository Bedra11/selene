"""
Styled distribution plot.
"""

import matplotlib.pyplot as plt

from .style import apply_style, COLORS


def styled_distribution(
    data,
    bins=10,
    title=None,
    xlabel=None,
    ylabel=None,
    highlight=False,
    show=True
):
    """
    Create a Selene-styled distribution plot (histogram).

    Parameters
    ----------
    data : list or array-like
        Numeric values.
    bins : int, default 10
        Number of bins.
    title : str, optional
        Title of the plot.
    xlabel : str, optional
        Label for the x-axis.
    ylabel : str, optional
        Label for the y-axis.
    highlight : bool, default False
        Use accent color instead of primary color.
    show : bool, default True
        Whether to display the plot immediately.
    """
    apply_style()

    color = COLORS["accent"] if highlight else COLORS["primary"]

    fig, ax = plt.subplots()

    ax.hist(
        data,
        bins=bins,
        color=color,
        edgecolor=COLORS["background"]
    )

    if title:
        ax.set_title(title)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)

    ax.margins(y=0.05)

    if show:
        plt.show()

    return fig, ax
