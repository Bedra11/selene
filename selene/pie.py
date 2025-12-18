# selene/pie.py
"""
Styled pie chart.
"""

import matplotlib.pyplot as plt

from .style import apply_style, COLORS


def styled_pie(
    values,
    labels,
    title=None,
    highlight_index=None,
    show=True
):
    """
    Create a Selene-styled pie chart.

    Parameters
    ----------
    values : list or array-like
        Values representing parts of a whole.
    labels : list
        Labels for each part.
    title : str, optional
        Title of the plot.
    highlight_index : int, optional
        Index of the slice to highlight using the accent color.
    show : bool, default True
        Whether to display the plot immediately.
    """
    apply_style()

    colors = [COLORS["secondary"]] * len(values)

    if highlight_index is not None and 0 <= highlight_index < len(values):
        colors[highlight_index] = COLORS["accent"]

    fig, ax = plt.subplots()

    ax.pie(
        values,
        labels=labels,
        colors=colors,
        startangle=90,
        wedgeprops={"edgecolor": COLORS["background"]}
    )

    if title:
        ax.set_title(title)

    ax.axis("equal")

    if show:
        plt.show()

    return fig, ax
