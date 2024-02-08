<img src='https://img.shields.io/badge/Difficulty-Medium-orange'>

<h5>Source: LeetCode</h5>

<h2>Problem statement</h2>

There is a singly-linked list head and we want to delete a node node in it.

You are given the node to be deleted node. You will not be given access to the first node of head.

All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

The value of the given node should not exist in the linked list.
<ul>
<li>The number of nodes in the linked list should decrease by one.</li>
<li>All the values before node should be in the same order.</li>
<li>All the values after node should be in the same order.</li>
</ul>

<h3>Examples:</h3>

Input: head = [4,5,1,9], node = 5

Output: [4,1,9]

Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

<h4>Constraints</h4>

The number of the nodes in the given list is in the range [2, 1000].

-1000 <= Node.val <= 1000

The value of each node in the list is unique.

The node to be deleted is in the list and is not a tail node.

<h2>Results:</h2>

<p>Runtime: 35 ms (faster than 83.18%)</p>
Memory usage: 16.8 MB (less than 80.66%)