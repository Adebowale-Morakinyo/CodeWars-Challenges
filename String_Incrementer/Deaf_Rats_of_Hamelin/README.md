# The Deaf Rats of Hamelin (2D)

Those pesky rats have returned and this time they have taken over the Town Square. The Pied Piper has been enlisted again to play his magical tune and coax all the rats towards him. But some of the rats are deaf and are going the wrong way!

## Kata Task

Your task is to determine how many deaf rats there are in the Town Square.

## Input Notes

- The Town Square is a rectangle of square paving stones (the Square has 1-15 pavers per side).
- The Pied Piper is always present.

## Output Notes

- Deaf rats are those that are moving to paving stones further away from the Piper than where they are now.
- Use Euclidean distance for your calculations.

## Legend

- `P`: The Pied Piper
- `←`, `↑`, `→`, `↓`, `↖`, `↗`, `↘`, `↙`: Rats going in different directions
- `space`: Everything else

## Implementation

The solution for the Deaf Rats of Hamelin challenge can be found in the `deaf_rats.py` file. The `count_deaf_rats(town_square)` function takes a 2D representation of the Town Square and calculates the number of deaf rats based on their movement in relation to the Pied Piper.

Feel free to explore the solutions and add your own CodeWars challenge solutions to the repository. Contributions and feedback are always welcome!

Happy coding! 🚀
