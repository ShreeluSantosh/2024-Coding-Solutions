<img src='https://img.shields.io/badge/Difficulty-Easy-green'>

<h3>Part of #LeetCode75 challenge</h3>

<h5>Source: LeetCode - LeetCode 75 study plan</h5>

<h2>Problem statement</h2>

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.

For example, abcde -> aecdb

Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.

For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

<h3>Example:</h3>

Input: word1 = "abc", word2 = "bca"

Output: true

Explanation: You can attain word2 from word1 in 2 operations.

Apply Operation 1: "abc" -> "acb"

Apply Operation 1: "acb" -> "bca"

<h4>Constraints</h4>

1 <= word1.length, word2.length <= 105

word1 and word2 contain only lowercase English letters.

<h2>Results:</h2>

<p>Runtime: 135 ms (faster than 65.36%)</p>
Memory usage: 18.5 MB (less than 18.96%)