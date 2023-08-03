# Hashtag Generator

The marketing team is spending way too much time typing in hashtags. Let's help them with our own Hashtag Generator!

## Challenge Description

Given an input string `s`, the Hashtag Generator must return a hashtag that adheres to the following rules:

1. It must start with a hashtag (#).
2. All words in the string must have their first letter capitalized.
3. If the final result is longer than 140 characters, it must return `False`.
4. If the input or the result is an empty string, it must also return `False`.

## Examples

- Input: `" Hello there thanks for trying my Kata"`
  Output: `#HelloThereThanksForTryingMyKata`

- Input: `"    Hello     World   "`
  Output: `#HelloWorld`

- Input: `""`
  Output: `False`

## Implementation

The solution for the Hashtag Generator challenge can be found in the `hashtag_generator.py` file. The `generate_hashtag(s)` function takes an input string `s` and returns the corresponding hashtag based on the specified rules.

Please feel free to explore the solutions and add your own CodeWars challenge solutions to the repository. Contributions and feedback are always welcome!

Happy coding! 🚀
