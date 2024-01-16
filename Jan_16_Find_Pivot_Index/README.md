<img src='https://img.shields.io/badge/Difficulty-Easy-green'>

<<h3>Part of #LeetCode75 challenge</h3>

<h5>Source: LeetCode - LeetCode 75 study plan</h5>

<h2>Problem statement</h2>

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

<h3>Example:</h3>

Input: nums = [1,7,3,6,5,6]

Output: 3

Explanation:

The pivot index is 3.

Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11

Right sum = nums[4] + nums[5] = 5 + 6 = 11

<h4>Constraints</h4>

1 <= nums.length <= 104

-1000 <= nums[i] <= 1000

<h2>Results:</h2>

<p>Runtime: 119 ms (faster than 93.15%)</p>
Memory usage: 18.5 MB (less than 26.33%)