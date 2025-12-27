# selene/style.py
"""
Selene global visual style.

Inspired by moonlight:
- calm illumination
- minimal decoration
- perceptually-aware defaults

This style prioritizes clarity, ethical representation,
and consistency across all visualizations.
"""

import matplotlib.pyplot as plt

# Color palette (Moonlight Minimal)

COLORS = {
    "background": "#F6F7F9",   # Soft lunar white
    "primary": "#1F2A44",      # Night blue
    "secondary": "#8A91A6",    # Mist gray
    "accent": "#C9B458",       # Moonlight gold
    "grid": "#E2E4E8",         # Subtle structure
}


# Typography and geometry

FONT_FAMILY = "DejaVu Sans"

LINE_WIDTH = 2.5
MARKER_SIZE = 6

SELENE_SEQ = [
    "#F6F7F9",  # background (very low)
    "#E2E4E8",  # grid
    "#C9CED8",
    "#AEB5C4",
    "#8A91A6",  # secondary
    "#6B738A",
    "#4C556F",
    "#2F3A55",
    "#1F2A44",  # primary (high)
]




# Style application

def apply_style():
    """
    Apply Selene's global matplotlib style.

    This function should be called at the beginning of every plot.
    """
    plt.rcParams.update({
        # Figure
        "figure.facecolor": COLORS["background"],
        "figure.autolayout": True,

        # Axes
        "axes.facecolor": COLORS["background"],
        "axes.edgecolor": COLORS["secondary"],
        "axes.labelcolor": COLORS["primary"],
        "axes.titleweight": "bold",
        "axes.titlecolor": COLORS["primary"],
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": False,

        # Ticks
        "xtick.color": COLORS["secondary"],
        "ytick.color": COLORS["secondary"],

        # Grid (disabled by default, available if needed)
        "grid.color": COLORS["grid"],
        "grid.linestyle": "-",
        "grid.linewidth": 0.8,

        # Text
        "text.color": COLORS["primary"],
        "font.family": FONT_FAMILY,

        # Lines & markers
        "lines.linewidth": LINE_WIDTH,
        "lines.markersize": MARKER_SIZE,
    })
