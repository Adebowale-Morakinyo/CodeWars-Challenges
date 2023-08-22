# Matrix Multiplier

## Description

In mathematics, a matrix (plural matrices) is a rectangular array of numbers. Matrices have many applications in programming, from performing transformations in 2D space to machine learning.

One of the most useful operations to perform on matrices is matrix multiplication, which takes a pair of matrices and produces another matrix – known as the dot product. Multiplying matrices is very different from multiplying real numbers and follows its own set of rules.

Unlike multiplying real numbers, multiplying matrices is non-commutative: in other words, multiplying matrix A by matrix B will not give the same result as multiplying matrix B by matrix A.

Additionally, not all pairs of matrices can be multiplied. For two matrices to be multipliable, the number of columns in matrix A must match the number of rows in matrix B.

To complete this kata, write a function that takes two matrices - A and B - and returns the dot product of those matrices. If the matrices cannot be multiplied, return null/None/Nothing or similar.

Each matrix will be represented by a two-dimensional list (a list of lists). Each inner list will contain one or more numbers, representing a row in the matrix.

For example, the following matrix:
```
|1 2|
|3 4|
```
Would be represented as:

```python
[[1, 2], [3, 4]]
```

It can be assumed that all lists will be valid matrices, composed of lists with equal numbers of elements, and which contain only numbers. The numbers may include integers and/or decimal points.

## Kata Link
[Matrix Multiplier](https://www.codewars.com/kata/573248f48e531896770001f9)

## Tags
Matrix, Algorithms, Linear Algebra, Mathematics