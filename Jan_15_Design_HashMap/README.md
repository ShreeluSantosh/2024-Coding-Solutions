<img src='https://img.shields.io/badge/Difficulty-Easy-green'>

<h5>Source: LeetCode - Linked Lists</h5>

<h2>Problem statement</h2>

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:
<ul>
<li>MyHashMap() initializes the object with an empty map.
<li>void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
<li>int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
<li>void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
</ul>

<h3>Example:</h3>

Input

["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]

[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]

Output

[null, null, null, 1, -1, null, 1, null, -1]

Explanation

MyHashMap myHashMap = new MyHashMap();

myHashMap.put(1, 1); // The map is now [[1,1]]

myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]

myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]

myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]

myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)

myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]

myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]

myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

<h4>Constraints</h4>

0 <= key, value <= 106

At most 104 calls will be made to put, get, and remove.

<h2>Results:</h2>

<p>Runtime: 160 ms (faster than 96.06%)</p>
Memory usage: 20.6 MB (less than 52.89%)