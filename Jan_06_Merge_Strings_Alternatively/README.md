<img src='https://img.shields.io/badge/Difficulty-Easy-green'>

<h2>Problem statement</h2>

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

<h4>Constraints</h4>

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.