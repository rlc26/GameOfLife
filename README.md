# Game of Life - Python Project

## Description

The **Game of Life** project implements John Conway's famous cellular automaton, using a representation of a world of cells and the rules that govern their evolution. This project makes it possible to run the game of life on a grid of cells and simulate its evolution over several generations.

## Prerequisites

Before you start, make sure you have the following installed:

- [Python 3.9+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation) for dependency and script management

## Installation

To install the project and its dependencies, follow the steps below:

1. Clone this repository:

   ```bash
   git clone https://github.com/EricBurnett/GameOfLife.git
   cd GameOfLife

2. Install dependencies using Poetry :

   ```bash
   poetry install

## Usage

Run the project to watch the simualation:

```bash
cd gameoflife
poetry run python life.py
```

## Controls

Up/Down/Left/Right: Pan the viewport

+/-: Speed up or slow down the rate of evolution

PageDown/PageUp: Zoom in/out

## Testing
To ensure the quality and correctness of the project, follow the steps below:

- Make sure you have installed all dependencies with poetry install as described above.
- Unit Testing :
   ```bash
   poetry run pytest
- Doctests :
   ```bash
   poetry run python -m doctest -v life.py
- Linting :
   ```bash
  poetry run pylint test
- Automatically check and fix common issues before code is committed :
  ```bash
  # Install pre-commit hooks
  pre-commit install
  # Optionally, run hooks on all files to ensure compliance
  pre-commit run --all-files
  ```

## Generating the Documentation

This project uses Sphinx to generate reference documentation from Python docstrings. Follow the steps below to generate the documentation:
1. Install the project dependencies, including Sphinx:
   ```bash
   poetry install
2. Generate the HTML documentation :
   ```bash
   poetry run make html
   ```
The generated documentation can be found in the docs/_build/html directory. Open index.html in your browser to view it.

## License

This project is licensed under the GNU Lesser General Public License (LGPL-3.0-or-later). See the [LICENSE](./LICENSE) file for details.

## Credits

Copyright (c) 2011 Eric Burnett.
Fork modifications (c) 2024 Romane.
