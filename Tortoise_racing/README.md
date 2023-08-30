# Tortoise Racing

## Problem Description

Two tortoises named A and B must run a race. A starts with an average speed of 720 feet per hour. Young B knows she runs faster than A, and furthermore has not finished her cabbage.

When she starts, at last, she can see that A has a 70 feet lead but B's speed is 850 feet per hour. How long will it take B to catch A?

More generally: given two speeds `v1` (A's speed, integer > 0) and `v2` (B's speed, integer > 0) and a lead `g` (integer > 0), how long will it take B to catch A?

The result will be an array `[hour, min, sec]` which is the time needed in hours, minutes, and seconds (rounded down to the nearest second) or a string in some languages.

If `v1 >= v2` then return `None`, `nothing`, `null`, `None`, or `[-1, -1, -1]` for certain languages.

## Examples

```python
race(720, 850, 70)  # Output: [0, 32, 18]
race(80, 91, 37)    # Output: [3, 21, 49]
```

## Notes

- Tortoises don't care about fractions of seconds.
- Think of calculation by hand using only integers (in your code use or simulate integer division).
- You can also Google: "convert decimal time to hours minutes seconds".

## Task Source

This problem is sourced from Codewars: [Tortoise racing](https://www.codewars.com/kata/55e2adece53b4cdcb900006c)
```
