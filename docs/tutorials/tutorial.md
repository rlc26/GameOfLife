# Tutorial: Build and Run Your Own Game of Life Simulation

## Introduction

In this tutorial, you will set up and run a simulation of Conway’s Game of Life. This step-by-step guide will help you prepare your environment, run the project, and explore the simulation interactively.

## What You Will Achieve

At the end of this tutorial, you will be able to:
    -Set up your environment for running the project.
    -Understand the project structure and its purpose.
    -Execute the simulation and interact with it.

## Step 1: Prepare Your Environment

### What You Need to Do

1. Install Python:
    Check if Python is installed by running:
    ```bash
    python3 --version
    ```
    If you don't have Python installed, you can download it from the official Python website: https://www.python.org/downloads/

2. Install Poetry:
    Follow the instructions on Poetry’s official site to install the tool:
    https://python-poetry.org/docs/

### What You Will Learn

In this step, you will learn how to set up your environment to run the project. You will install Python and Poetry, which are essential tools for managing the project’s dependencies and packaging.

## Step 2: Clone the Repository

### What You Need to Do

Clone the project repository to your local machine:
```bash
git clone https://github.com/rlc26/GameOfLife.git
cd GameOfLife
```
💡 Note: Replace `rlc26` with your GitHub username if you forked the repository.

### What You Will Learn

In this step, you will learn how to clone the project repository to your local machine. This allows you to access the project's source code and make changes if needed.

### 💡 Tip

If you encounter any issues while cloning the repository, ensure that you have Git installed on your machine. You can download Git from the official Git website: https://git-scm.com/downloads

## Step 3: Install Dependencies

### What You Need to Do

Install the required dependencies using Poetry:
```bash
poetry install
```

### What You Will Learn

In this step, you will learn how to install the necessary dependencies for the project using Poetry.

### 💡 Tip
Ensure you have activated the virtual environment created by Poetry before running any commands.
You can activate it with:
```bash
source .venv/bin/activate
```


## Step 4: Run the Simulation

### What You Need to Do

Launch the main script to start the Game of Life simulation:
```bash
poetry run python game_of_life/life.py
```

### What You Should See

A graphical window will open, showing the grid of cells evolving over generations.

### What You Will Learn

In this step, you will learn how to run the main script of the project to start the Game of Life simulation.

## Step 5: Explore and Customize the Simulation

### What You Can Do

- Edit the `life.py` file to customize the initial state of the simulation.
- Add your own patterns and observe how they evolve.
- Experiment with modifying the rules or the grid size to see different results.

## Expected Results

At each step, you should see concrete outcomes:
- The console will confirm that the simulation is running.
- The graphical interface will display a grid of cells, evolving according to Conway’s rules.

## Conclusion

Congratulations! You have successfully installed the project, set up the environment, and run the Game of Life simulation. Feel free to explore and customize the simulation to further your understanding of cellular automata and Conway’s Game of Life.
