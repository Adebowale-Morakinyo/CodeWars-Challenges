# Range Extraction

A format for expressing an ordered list of integers is to use a comma-separated list of either:

- Individual integers.
- A range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval, including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example, "12,13,15-17".

## Problem Description

Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

## Example

```python
solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
```

Courtesy of [Rosetta Code](https://rosettacode.org).

## Implementation Details

- The function `solution(args)` takes a list of integers `args` in increasing order.
- It iterates through the list and identifies continuous ranges of numbers.
- If a range contains three or more numbers, it is formatted as "start-end".
- If a range contains less than three numbers, each number is individually included in the result.
- Finally, the function returns a string where the formatted ranges and individual numbers are comma-separated.

## Constraints

- The input list `args` is sorted in ascending order.
- The integers in the input list are within the 32-bit signed integer range.

## Note

- There can be multiple valid solutions for this problem, as long as they follow the formatting rules.
