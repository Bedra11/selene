# Selene 

Selene is a lightweight Python visualization library focused on clarity, consistency, and perceptual accuracy.

Inspired by the idea of moonlight — calm illumination without visual noise — Selene provides a small set of opinionated plotting functions designed for clear and ethical data representation.

The library emphasizes:

- Minimal visual design
- Consistent styling across plots
- Readable defaults without unnecessary decoration

Selene is built on top of `matplotlib` and is intended for simple, clean visualizations rather than exhaustive customization.


## Installation

Install Selene locally (editable mode):

```bash
pip install -e .
```


## Usage

After installation, Selene can be imported and used directly in any Python script.

### Line Plot

```python
import selene

selene.styled_line(
    x=[1, 2, 3, 4],
    y=[2, 3, 2.5, 4],
    title="Trend over time",
    xlabel="Time",
    ylabel="Value"
)
```

### Bar Chart

```python
selene.styled_bar(
    categories=["A", "B", "C"],
    values=[10, 15, 7],
    title="Category comparison",
    ylabel="Value"
)
```

### Scatter Plot

```python
selene.styled_scatter(
    x=[1, 2, 3, 4],
    y=[2, 2.5, 3.2, 4.1],
    title="Relationship between variables"
)
```

### Distribution

```python
selene.styled_distribution(
    data=[1, 2, 2, 3, 3, 3, 4, 5],
    bins=5,
    title="Value distribution"
)
```

### Pie Chart

```python
selene.styled_pie(
    values=[50, 30, 20],
    labels=["A", "B", "C"],
    title="Composition example"
)
```

---

## Design Philosophy

Selene is intentionally minimal and opinionated.

Rather than exposing all possible styling options, it provides consistent defaults that prioritize readability and perceptual clarity. The goal is to let the data speak clearly, without unnecessary visual emphasis.

---

## License

Selene is distributed under the MIT License.
