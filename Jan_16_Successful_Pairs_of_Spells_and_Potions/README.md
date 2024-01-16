<img src='https://img.shields.io/badge/Difficulty-Medium-orange'>

<<h3>Part of #LeetCode75 challenge</h3>

<h5>Source: LeetCode - LeetCode 75 study plan</h5>

<h2>Problem statement</h2>

You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

<h3>Example:</h3>

Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7

Output: [4,0,3]

Explanation:

- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.

Thus, [4,0,3] is returned.

<h4>Constraints</h4>

n == spells.length

m == potions.length

1 <= n, m <= 105

1 <= spells[i], potions[i] <= 105

1 <= success <= 1010

<h2>Results:</h2>

<p>Runtime: 1328 ms (faster than 53.94%)</p>
Memory usage: 40.3 MB (less than 30.02%)