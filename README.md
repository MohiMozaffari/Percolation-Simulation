# Percolation Simulation

## Introduction

This repository contains Python code for simulating percolation on a square lattice using a depth-first search algorithm. Percolation is a phenomenon where liquid or gas passes through a porous material, and it has applications in various fields, including physics, chemistry, and hydrology.

## Getting Started

To run the simulation, follow these steps:

1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Install the required dependencies by running:
```bash
pip install numpy matplotlib seaborn
```
4. Run the script `percolation_simulation.py`:

```bash
python percolation_simulation.py
```
## Code Structure
The code consists of the following main parts:

newgrid(p, N=100): Creates a new grid of size N by N with a probability of p for each cell to be filled.

walk(m, n, grid, nwalk): Performs a depth-first search to identify the connected component and mark it with a unique identifier.

check(grid): Checks the grid for percolation from the top row and marks the connected components.

CountFrequency(my_list): Counts the frequency of connected components.

## Parameters
p: Probability of each cell being filled.

N: Size of the grid.

## Visualization
The simulation results are visualized using Seaborn's heatmap, showing the percolated grid with different colors representing connected components. The size of the giant component is calculated and displayed in the title of the plot.

## Output
The simulation generates a heatmap plot of the percolated grid, saved as a PNG file.
