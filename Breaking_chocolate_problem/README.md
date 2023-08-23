# Breaking Chocolate Problem

Your task is to split a chocolate bar of given dimensions `n x m` into small squares. Each square is of size `1x1` and unbreakable. Implement a function that will return the minimum number of breaks needed.

## Task

Write a function `break_chocolate(n, m)` that takes two integer arguments `n` and `m`, representing the dimensions of the chocolate bar, and returns the minimum number of breaks needed.

## Examples

- `break_chocolate(2, 1)` should return `1` (1 break to split into individual squares).
- `break_chocolate(3, 1)` should return `2` (2 breaks to split into individual squares).
- `break_chocolate(0, 5)` should return `0` (no breaks needed for an invalid input dimension).

## Constraints

- The input dimensions `n` and `m` will always be non-negative integers.

## Usage

```python
result = break_chocolate(2, 1)
print(result)  # Output: 1
```

## Contributing
If you have a better solution or any improvements, feel free to contribute by submitting a pull request.

## Related Kata
This kata is categorized under algorithms.