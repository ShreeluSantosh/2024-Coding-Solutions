<img src='https://img.shields.io/badge/Difficulty-Medium-orange'>

<h3>Part of #LeetCode75 challenge</h3>

<h5>Source: LeetCode - LeetCode 75 study plan</h5>

<h2>Problem statement</h2>

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

<h3>Example:</h3>

Input: nums = [1,2,3,4], k = 5

Output: 2

Explanation: Starting with nums = [1,2,3,4]:

- Remove numbers 1 and 4, then nums = [2,3]

- Remove numbers 2 and 3, then nums = []

There are no more pairs that sum up to 5, hence a total of 2 operations.

<h4>Constraints</h4>

1 <= nums.length <= 105

1 <= nums[i] <= 109

1 <= k <= 109

<h2>Results:</h2>

<p>Runtime: 496 ms (faster than 90.85%)</p>
Memory usage: 29.5 MB (less than 58.40%)