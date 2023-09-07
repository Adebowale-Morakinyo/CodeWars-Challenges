# Conway's Game of Life - Unlimited Edition

## Problem Description

Given a 2D array and a number of generations, compute n timesteps of Conway's Game of Life.

The rules of the game are as follows:

1. Any live cell with fewer than two live neighbors dies, as if caused by underpopulation.
2. Any live cell with more than three live neighbors dies, as if by overcrowding.
3. Any live cell with two or three live neighbors lives on to the next generation.
4. Any dead cell with exactly three live neighbors becomes a live cell.

Each cell's neighborhood is the 8 cells immediately around it (i.e., Moore Neighborhood). The universe is infinite in both the x and y dimensions, and all cells are initially dead, except for those specified in the arguments. The return value should be a 2D array cropped around all of the living cells. If there are no living cells, then return `[[]]`.

For illustration purposes, 0 and 1 will be represented as ░░ and ▓▓ blocks, respectively. You can take advantage of the `htmlize` function to get a text representation of the universe.

**Example:**

```python
cells = [[1, 0, 0], [0, 1, 1], [1, 1, 0]]
generations = 1
get_generation(cells, generations)  # Output: [[0, 1, 0], [0, 0, 1], [1, 1, 1]]
```

## Function Signature

Your function should be named `get_generation` and should take two parameters:
- `cells`: A 2D array representing the initial state of cells.
- `generations`: An integer representing the number of generations to compute.

Your function should return a 2D array representing the state of cells after `generations` timesteps.

## Notes

- The universe is infinite, but you only need to compute the state of cells within the cropped region.
- You can assume that the input `cells` is a valid 2D array of 0s and 1s.

## Task Source

This problem is sourced from Codewars: [Conway's Game of Life - Unlimited Edition](https://www.codewars.com/kata/conways-game-of-life-unlimited-edition)
