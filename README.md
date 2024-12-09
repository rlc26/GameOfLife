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

## Static Code Analysis and Testing
To ensure the quality and correctness of the project, you can run unit tests, doctests, and lint checks. Follow the steps below:

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


## Project execution
To run the project and watch the game in action, you can use the project's life.py code.
```bash
cd gameoflife
poetry run python life.py
```

## Building a package
To generate a project package (for example, a .tar.gz or .whl file), you can use the following command:
```bash
poetry build
```
The generated files will be placed in the project's dist/ folder.

## Version Control
- To increase the minor version :
    ```bash
    poetry version minor
- To increase the major version :
    ```bash
    poetry version major
- To upgrade the patch :
    ```bash
    poetry version patch


## Controls

Up/Down/Left/Right: Pan the viewport

+/-: Speed up or slow down the rate of evolution

PageDown/PageUp: Zoom in/out

## Credits

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

The full text of the GNU Lesser General Public License is included in the LICENSE file accompanying this program.

Copyright (c) 2011 Eric Burnett.
Fork modifications (c) 2024 Romane.
