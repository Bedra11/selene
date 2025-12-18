"""
Styled scatter plot for exploring relationships between two quantitative variables.
"""
import matplotlib.pyplot as plt

from .style import apply_style, COLORS


def styled_scatter(
    x,
    y,
    title=None,
    xlabel=None,
    ylabel=None,
    alpha=0.7,
    highlight=False,
    show=True
):
    """
    Create a Selene-styled scatter plot.

    Parameters
    ----------
    x : list or array-like
        Values for the x-axis.
    y : list or array-like
        Values for the y-axis.
    title : str, optional
        Title of the plot.
    xlabel : str, optional
        Label for the x-axis.
    ylabel : str, optional
        Label for the y-axis.
    alpha : float, default 0.7
        Transparency to reduce overplotting.
    highlight : bool, default False
        Use accent color instead of primary color.
    show : bool, default True
        Whether to display the plot immediately.
    """
    apply_style()

    color = COLORS["accent"] if highlight else COLORS["primary"]

    fig, ax = plt.subplots()

    ax.scatter(
    x,
    y,
    color=color,
    alpha=alpha,
    edgecolors=COLORS["background"],
    linewidths=0.6
)


    if title:
        ax.set_title(title)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)

    ax.margins(x=0.05, y=0.05)

    if show:
        plt.show()

    return fig, ax
