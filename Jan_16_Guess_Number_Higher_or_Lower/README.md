<img src='https://img.shields.io/badge/Difficulty-Easy-green'>

<<h3>Part of #LeetCode75 challenge</h3>

<h5>Source: LeetCode - LeetCode 75 study plan</h5>

<h2>Problem statement</h2>

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:
<ul>
<li>-1: Your guess is higher than the number I picked (i.e. num > pick).
<li>1: Your guess is lower than the number I picked (i.e. num < pick).
<li>0: your guess is equal to the number I picked (i.e. num == pick).
</ul>
Return the number that I picked.

<h3>Example:</h3>

Input: n = 10, pick = 6

Output: 6

<h4>Constraints</h4>

1 <= n <= 231 - 1

1 <= pick <= n

<h2>Results:</h2>

<p>Runtime: 45 ms (faster than 16.44%)</p>
Memory usage: 17.2 MB (less than 44.61%)