# mathlib

A mathematical library for Python, designed to provide practical mathematical tools while implementing its functionality independently from Python's built-in `math` module.

## Overview

**mathlib** is a Python mathematical library developed by **Natanael Rodrigues**.

The project was created as a practical study and development project focused on implementing mathematical concepts in Python while building a reusable library.

The library includes functionality for areas such as:

- Probability
- Statistics
- Combinatorics
- Functions
- Analytic geometry
- Plane geometry
- Spatial geometry

The project also uses object-oriented programming where appropriate, allowing mathematical concepts to be represented through reusable classes and structures.

## Features

- Mathematical functions implemented independently
- No dependency on Python's built-in `math` module
- Geometry classes using object-oriented programming
- Probability calculations
- Statistical functionality
- Combinatorial calculations
- Function-related operations
- Input validation helpers
- Reusable mathematical components

## Modules

The library is organized into specialized modules:

### `analytic_geometry`

Tools related to analytical geometry.

### `combinatorics`

Functions for combinatorial calculations and mathematical counting.

### `function`

Function-related mathematical operations.

### `plan_geometry`

Tools for plane geometry.

### `probability`

Functions for probability calculations, including:

- Probability
- Complement probability
- Conditional probability
- Joint probability
- Union probability

### `spatial_geometry`

Tools for spatial and three-dimensional geometry.

### `statistic`

Functions related to statistics and statistical calculations.

## Constants

The library defines mathematical constants directly instead of relying on the `math` module.

```python
PI = 3.141592653589793
EULER = 2.718281828459045
```

## Validation

The library includes validation helpers to ensure that functions receive appropriate values.

Examples include:

```python
validate_values(...)
```

and

```python
validate_coefficient(...)
```

These helpers are used to keep mathematical operations consistent and prevent invalid input from being processed.

## Installation

Install the package from PyPI using:

```bash
pip install advancedmath-natcar2000
```

## Usage

After installation, import the required components from the library.

Example:

```python
from advancedmath import ...
```

The exact import path may vary depending on the module being used.

## Requirements

- Python 3.10 or newer

## Project Structure

A simplified representation of the project structure:

```text
mathlib/
│
├── analytic_geometry/
├── combinatorics/
├── function/
├── plan_geometry/
├── probability/
├── spatial_geometry/
├── statistic/
│
├── pyproject.toml
└── README.md
```

## Development Philosophy

mathlib is not intended to simply wrap existing mathematical libraries.

The project focuses on understanding and implementing mathematical concepts directly in Python.

The main goals are:

- Learn through implementation
- Practice mathematical reasoning
- Develop reusable software
- Improve Python programming skills
- Explore object-oriented design
- Build a practical mathematical library

## Version

Current version:

```text
1.0.2
```

## License

This project is licensed under the **GNU General Public License (GPL)**.

See the `LICENSE` file for more information.

## Author

**Natanael Rodrigues**

GitHub:

`natcar2000`

## Project Status

mathlib is an evolving project.

New mathematical functionality may be added over time as the library grows and new concepts are implemented.

---

**mathlib — Learn mathematics by implementing it.**
