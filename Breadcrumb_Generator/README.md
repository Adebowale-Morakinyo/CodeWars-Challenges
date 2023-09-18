# Breadcrumb Generator

Breadcrumb menus are a popular way to display a user's path through a website. This kata challenges you to create a function that takes a URL, extracts the relevant components, and generates a breadcrumb trail for navigation.

## Problem Statement

Given a URL and a separator, you need to generate a breadcrumb trail. The first part of the URL is always labeled "HOME," and the rest of the components form a navigation trail, with each component being a clickable link except for the last one, which is marked as active.

The rules for generating breadcrumbs are as follows:

1. The URL components are turned to uppercase.
2. The last element can end with common extensions like `.html`, `.htm`, `.php`, or `.asp`. If the last element is `index.something`, it should be treated as if it's not there.
3. If a component (except for the root/home) is longer than 30 characters, it should be shortened by acronymizing it (using the initials of each word).
4. Words in the list `["the", "of", "in", "from", "by", "with", "and", "or", "for", "to", "at", "a"]` should be ignored during acronymization.
5. Ignore anchors (e.g., `#example`) and parameters (e.g., `?codewars=rocks&pippi=rocksToo`) if they are present.
6. Components should be separated by the provided separator.

## Examples

Here are some example inputs and expected outputs:

- Input: `generate_bc("mysite.com/pictures/holidays.html", " : ")`
  Output: `<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> : <span class="active">HOLIDAYS</span>`

- Input: `generate_bc("www.codewars.com/users/GiacomoSorbi?ref=CodeWars", " / ")`
  Output: `<a href="/">HOME</a> / <a href="/users/">USERS</a> / <span class="active">GIACOMOSORBI</span>`

## Notes

- You will always be provided valid URLs in common formats, so you don't need to validate them.

## Testing

You can use the provided test cases to verify the correctness of your solution.

## Constraints

- The maximum length of the input URL is 10^5 characters.
- The separator will be a non-empty string.
