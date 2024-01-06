<img src='https://img.shields.io/badge/Difficulty-Medium-orange'>

<h3>Part of #LeetCode75 challenge</h3>

<h5>Source: LeetCode - LeetCode 75 study plan</h5>

<h2>Problem statement</h2>

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

<p>If the group's length is 1, append the character to s.</p>
<p>Otherwise, append the character followed by the group's length.</p>
<p>The compressed string s should not be returned separately, but instead, be stored in the input character array chars.</p>
<p>Note that group lengths that are 10 or longer will be split into multiple characters in chars.</p>

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

<h3>Example:</h3>

<p>Input: chars = ["a","a","b","b","c","c","c"]</p>
<p>Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]</p>
<p>Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".</p>

<h4>Constraints</h4>

<p>1 <= chars.length <= 2000</p>
<p>chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.</p>

<h2>Results:</h2>

<p>Runtime: 66 ms (faster than 53.49%)</p>
Memory usage: 17.2 MB (less than 8.38%)