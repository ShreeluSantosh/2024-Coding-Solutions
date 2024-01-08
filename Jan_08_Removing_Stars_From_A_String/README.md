<img src='https://img.shields.io/badge/Difficulty-Medium-orange'>

<h3>Part of #LeetCode75 challenge</h3>

<h5>Source: LeetCode - LeetCode 75 study plan</h5>

<h2>Problem statement</h2>

You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.

Remove the closest non-star character to its left, as well as remove the star itself.

Return the string after all stars have been removed.

<h3>Example:</h3>

Input: s = "leet**cod*e"

Output: "lecoe"

Explanation: Performing the removals from left to right:

- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".

- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".

- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".

There are no more stars, so we return "lecoe".

<h4>Constraints</h4>

1 <= s.length <= 105

s consists of lowercase English letters and stars *.

The operation above can be performed on s.

<h2>Results:</h2>

<p>Runtime: 131 ms (faster than 95.17%)</p>
Memory usage: 19 MB (less than 22.74%)