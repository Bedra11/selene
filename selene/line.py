"""
Styled line chart for the Selene visualization library.

Use this plot to show trends or evolution over an ordered axis
(e.g. time, sequence, continuous values).
"""

import matplotlib.pyplot as plt

from .style import apply_style, COLORS


def styled_line(
    x,
    y,
    title=None,
    xlabel=None,
    ylabel=None,
    highlight=None,
    show=True
):
    """
    Create a Selene-styled line chart.

    Parameters
    ----------
    x : list or array-like
        Values for the x-axis.
    y : list, array-like, or dict
        Single series (list) or multiple series as a dict {label: values}.
    highlight : str or None
        Label of the series to highlight (for multi-line plots).
    """
    apply_style()

    fig, ax = plt.subplots()

    # Case 1: single line
    if not isinstance(y, dict):
        ax.plot(x, y, color=COLORS["primary"])

    # Case 2: multiple lines
    else:
        for label, values in y.items():
            color = COLORS["accent"] if label == highlight else COLORS["primary"]
            ax.plot(x, values, label=label, color=color, alpha=0.85)

        ax.legend(frameon=False)

    if title:
        ax.set_title(title)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)

    ax.margins(x=0.02)

    if show:
        plt.show()

    return fig, ax
