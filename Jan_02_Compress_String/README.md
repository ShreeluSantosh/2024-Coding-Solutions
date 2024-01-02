<img src='https://img.shields.io/badge/Difficulty-Medium-orange'>

<h2>Problem statement</h2>

Ninja has been given a program to do basic string compression. For a character that is consecutively repeated more than once, he needs to replace the consecutive duplicate occurrences with the count of repetitions.

Example:

If a string has 'x' repeated 5 times, replace this "xxxxx" with "x5".

The string is compressed only when the repeated character count is more than 1.

Note :

The consecutive count of every character in the input string is less than or equal to 9.

<h4>Sample Input 1:</h4>

2

aaabbddccc

ggttttffffrreee

<h4>Sample Output 1:</h4>

a3b2d2c3

g2t4f4r2e3

<h4>Explanation of Sample Input 1:</h4>

Test case 1:

For the first test case of sample output 1, our compressed string is “a3b2d2c3”. It represents that the string contains 3 consecutive ‘a’, 2 consecutive ‘b’, 2 consecutive ‘d’, and 3 consecutive ‘c’.
