<img src='https://img.shields.io/badge/Difficulty-Medium-orange'>

<<h3>Part of #LeetCode75 challenge</h3>

<h5>Source: LeetCode - LeetCode 75 study plan</h5>

<h2>Problem statement</h2>

You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

<h3>Example:</h3>

Input: head = [1,3,4,7,1,2,6]

Output: [1,3,4,1,2,6]

Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.

Since n = 7, node 3 with value 7 is the middle node, which is marked in red.

We return the new list after removing this node.

<h4>Constraints</h4>

The number of nodes in the list is in the range [1, 105].

1 <= Node.val <= 105

<h2>Results:</h2>

<p>Runtime: 658 ms (faster than 72.59%)</p>
Memory usage: 51.4 MB (less than 75.17%)