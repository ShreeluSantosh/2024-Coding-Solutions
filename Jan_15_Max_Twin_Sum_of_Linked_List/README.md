<img src='https://img.shields.io/badge/Difficulty-Medium-orange'>

<<h3>Part of #LeetCode75 challenge</h3>

<h5>Source: LeetCode - LeetCode 75 study plan</h5>

<h2>Problem statement</h2>

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

<h3>Example:</h3>

Input: head = [5,4,2,1]

Output: 6

Explanation:

Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.

There are no other nodes with twins in the linked list.

Thus, the maximum twin sum of the linked list is 6. 

<h4>Constraints</h4>

The number of nodes in the list is an even integer in the range [2, 105].

1 <= Node.val <= 105

<h2>Results:</h2>

<p>Runtime: 326 ms (faster than 98.63%)</p>
Memory usage: 32.8 MB (less than 97.42%)