# Game of Life - Python Project

## Description

The **Game of Life** project implements John Conway's famous cellular automaton, using a representation of a world of cells and the rules that govern their evolution. This project makes it possible to run the game of life on a grid of cells and simulate its evolution over several generations.

## Prerequisites

Before you start, make sure you have the following installed:

- [Python 3.8+](https://www.python.org/downloads/)
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

## Tests
To run unit tests on the project, follow the steps below:

- Make sure you have installed all dependencies with poetry install as described above.
- Run the tests with Poetry and pytest :
   ```bash
   poetry run pytest

## Project execution
To run the project and watch the game in action, you can use the project's life.py code.
    ```bash
   cd gameoflife
   poetry run python life.py

## Building a package
To generate a project package (for example, a .tar.gz or .whl file), you can use the following command:
    ```bash
    poetry build
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

Game of Life, copyright Eric Burnett, 2011.

All code available under the LGPL (or most other licenses you might want).

Contact me if you need me to stuff on appropriate headers.
