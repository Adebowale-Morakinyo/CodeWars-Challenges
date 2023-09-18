# So Many Permutations!

In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.

Create as many "shufflings" as you can!

## Problem Description

Write a function that takes a non-empty input string and generates all possible permutations of that string, removing any duplicates.

## Examples

- With input `'a'`:
  Your function should return: `['a']`

- With input `'ab'`:
  Your function should return `['ab', 'ba']`

- With input `'abc'`:
  Your function should return `['abc','acb','bac','bca','cab','cba']`

- With input `'aabb'`:
  Your function should return `['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']`

Note: The order of the permutations doesn't matter.

## Implementation Details

- The function `generate_permutations(input_str)` takes a non-empty input string `input_str`.
- It generates all possible permutations of the input string.
- Duplicates are removed, ensuring that each permutation in the result list is unique.
- The result is a list of strings, where each string is a unique permutation of the input string.

## Constraints

- The input string `input_str` is non-empty.

Absolutely, let's provide a clear explanation of how the code utilizes `itertools.permutations` from the `itertools` library to solve the challenge:

## The Power of itertools

Python's `itertools` library is a versatile collection of tools for working with iterators. Among these tools, we find `itertools.permutations`, which generates all possible permutations of an input sequence.

## How the Code Works

The heart of this code is the `permutations` function. It takes an input string and returns a list of unique permutations. Here's how it's done:

1. **Generate Permutations**: We leverage `itertools.permutations` to create all possible permutations of the input string. These permutations are generated as tuples, so we have to convert them back to strings.

2. **Remove Duplicates with a Set**: The permutations generated by `itertools.permutations` may include duplicates. To ensure uniqueness, we use a Python set. Sets automatically remove duplicate elements, so we end up with a collection of unique permutations.

3. **Convert Back to a List**: While sets are efficient for duplicate removal, we convert the set back into a list. This is because the challenge requires us to return the permutations as a list.

4. **Joining Characters**: To convert each permutation tuple back to a string, we use a simple `''.join()` operation. This transforms the characters in each permutation tuple into a single string.

5. **Return the Result**: The function returns the list of unique permutations, as required by the challenge.

## Examples

Let's illustrate how the code works with some examples:

- For input `'a'`, the function returns `['a']`. Since there's only one character, there's only one permutation: `'a'`.

- For input `'ab'`, the function returns `['ab', 'ba']`. Two characters result in two unique permutations.

- For input `'aabb'`, the function returns `['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']`. Here, four characters, some of which are repeated, generate six unique permutations.