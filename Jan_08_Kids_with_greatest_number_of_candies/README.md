<img src='https://img.shields.io/badge/Difficulty-Easy-green'>

<h3>Part of #LeetCode75 challenge</h3>

<h5>Source: LeetCode - LeetCode 75 study plan</h5>

<h2>Problem statement</h2>

There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

<h3>Example:</h3>

Input: candies = [2,3,5,1,3], extraCandies = 3

Output: [true,true,true,false,true] 

Explanation: If you give all extraCandies to:

- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.

- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.

- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.

- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

<h4>Constraints</h4>

n == candies.length

2 <= n <= 100

1 <= candies[i] <= 100

1 <= extraCandies <= 50

<h2>Results:</h2>

<p>Runtime: 58 ms (faster than 11.39%)</p>
Memory usage: 16.4 MB (less than 52.24%)