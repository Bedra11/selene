# selene/bar.py
"""
Styled bar chart for comparing values across discrete categories.
"""

import matplotlib.pyplot as plt
import numpy as np

from .style import apply_style, COLORS


def styled_bar(
    categories,
    values=None,
    series=None,
    title=None,
    ylabel=None,
    show=True
):
    apply_style()

    fig, ax = plt.subplots()

    x = np.arange(len(categories))

    # Single-series bar chart
    if values is not None:
        ax.bar(x, values, color=COLORS["primary"])
        ax.set_xticks(x)
        ax.set_xticklabels(categories)

    # Multi-series bar chart
    elif series is not None:
        n_series = len(series)
        width = 0.8 / n_series

        for i, (label, vals) in enumerate(series.items()):
            ax.bar(
                x + i * width,
                vals,
                width=width,
                label=label,
                color=COLORS["primary"] if i == 0 else COLORS["secondary"]
            )

        ax.set_xticks(x + width * (n_series - 1) / 2)
        ax.set_xticklabels(categories)
        ax.legend(frameon=False)

    else:
        raise ValueError("Either 'values' or 'series' must be provided.")

    ax.set_ylim(bottom=0)

    if title:
        ax.set_title(title)
    if ylabel:
        ax.set_ylabel(ylabel)

    ax.margins(y=0.05)

    if show:
        plt.show()

    return fig, ax
