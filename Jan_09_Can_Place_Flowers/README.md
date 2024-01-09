<img src='https://img.shields.io/badge/Difficulty-Easy-green'>

<h3>Part of #LeetCode75 challenge</h3>

<h5>Source: LeetCode - LeetCode 75 study plan</h5>

<h2>Problem statement</h2>

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

<h3>Example:</h3>

Input: flowerbed = [1,0,0,0,1], n = 1

Output: true

Input: flowerbed = [1,0,0,0,1], n = 2

Output: false

<h4>Constraints</h4>

1 <= flowerbed.length <= 2 * 104

flowerbed[i] is 0 or 1.

There are no two adjacent flowers in flowerbed.

0 <= n <= flowerbed.length

<h2>Results:</h2>

<p>Runtime: 137 ms (faster than 83.13%)</p>
Memory usage: 17.7 MB (less than 23.32%)