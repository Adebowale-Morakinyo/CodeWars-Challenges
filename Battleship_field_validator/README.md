# Battleship Field Validator

This is a solution for the "Battleship Field Validator" kata on Codewars.

## Description

Write a method that takes a field for the well-known board game "Battleship" as an argument and returns `True` if it has a valid disposition of ships, `False` otherwise. The argument is guaranteed to be a 10x10 two-dimensional array. Elements in the array are numbers, where 0 represents a free cell and 1 represents a cell occupied by a ship.

Battleship (also known as Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid containing several "ships," and the objective is to destroy the enemy's forces by targeting individual cells on their field.

## Rules

Before the game begins, players set up the board and place the ships according to the following rules:

- There must be a single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2), and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
- Each ship must be in a straight line, except for submarines, which are single cells.
- Ships cannot overlap or be in contact with any other ship, neither by edge nor by corner.

## Solution

The provided Python solution validates whether the given field adheres to the rules for placing ships in the Battleship game. It uses depth-first search (DFS) to identify and count ships of different sizes. The ship sizes are then compared with the expected count to determine if the field is valid.

## Usage

To use the `validate_battlefield` function, pass a 10x10 two-dimensional array representing the Battleship field. Elements in the array should be either 0 (free cell) or 1 (occupied by a ship).

Example usage:

```python
field = [
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print(validate_battlefield(field))  # Output: True
```

## Contributing

Feel free to contribute to this solution by suggesting improvements or optimizations.
