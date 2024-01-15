<img src='https://img.shields.io/badge/Difficulty-Medium-orange'>

<<h3>Part of #LeetCode75 challenge</h3>

<h5>Source: LeetCode - LeetCode 75 study plan</h5>

<h2>Problem statement</h2>

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

<h3>Example:</h3>

Input: asteroids = [10,2,-5]

Output: [10]

Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

<h4>Constraints</h4>

2 <= asteroids.length <= 104

-1000 <= asteroids[i] <= 1000

asteroids[i] != 0

<h2>Results:</h2>

<p>Runtime: 79 ms (faster than 93.23%)</p>
Memory usage: 18.4 MB (less than 39.22%)