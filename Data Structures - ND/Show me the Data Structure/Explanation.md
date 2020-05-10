# Problem 1 - LRU Cache
### Approach
- I used a Ordered dictionary to hold the key and value pair.
- I popped the element and added again whenever it was accessed so that the element which was accessed least would stay at the end.
### Efficiency
- As required, I tried to keep all operation within a complexity of O(1) and chose the data structures accordingly. 

# Problem 2 - Find files
### Approach
- I used recursion for this approach where in I was recursively iterating through all the directories and files. I had to append the parent directory and extend in the recursive case for building the list. 
### Efficiency
- Each file is only inspected once. According to the Python wiki entry on time complexity, this has O(n) n being number files.

# Problem 3 - Huffman Encoding
### Approach
- First I found out frequency for each character in the text and created a node with data and frequency. I used a list to append these nodes, once done I had to sort it in reverse to maintain least frequencies at the end to perform `pop()` to get least two nodes in the list.
- Once the list was sorted I recursively kept popping the least two nodes and joining to a parent node which had sum of their frequencies. I did this until I had only one node in the list which would be head of the Huffman's tree.
- Once the Tree was created I used a dictionary to store the encoded values retrieved after traversing the tree. Similarly I used the same dictionary to decode the letters by traversing through the encoded text.
### Efficiency
- For Big O we loop over all characters, we then loop over all frequencies to make the heap. We also recurse through the tree when making the map of characters to binary code. So I believe our performance is `O(n)` as I'm iterating each character in a linear fashion and making the worst case scenario time `O(h)` where h is height of Huffman's tree. 
- And O(n log n) for sorting the list of nodes with character and frequencies. Overall time complexity would be `O(n)+O(h)+O(n log n)`

Finally Big O Notation would be: `O(n log n)` is more dominant when compared to other Big - O Notations.

# Problem 4 - User in group 
### Approach
- This was straightforward for a recursive algorithm that exits once the answer is clearly true or false, respectively.

### Efficiency
- The time complexity of this algorithm is dependant on the number of iterations in the recursive stack. 
- Being in this case dependent on encapsulation of groups and number of users of folders, resulting in a `O(g*u)`

# Problem 5 - Blockchain
### Approach
- The problem statement didn't specify any requirements, so I chose a simple lined list to build the blockchain. This allows simple appending, I added test function to verify to make the problem slightly more interesting by checking the hash values. 

### Efficiency
- This algorithm has a complexity of 
    - `O(1)` for `add_block()`
    - `O(n)` for `get_block()`
    - `O(1)` for `capacity()`
    - `O(n)` for `to_list()`

# Problem 6 - List union & intersection
### Approach
- The problem statement didn't specify any requirements as in What must be the order? Does it have duplicates?  In my solution, duplicates are removed, as I have used `set()`.
- I have used built-in functions provided by `set()` for `union()` and `intersection()`

### Efficiency
- The time complexity for converting `set()` to a linkedlist, takes `O(n)` as I'm appending elements linearly
- The union algorithm has a complexity of O(n) after creating of final set() for appending to the LinkedList.
- The [python wiki](https://wiki.python.org/moin/TimeComplexity) on time complexity lists a single intersection as `O(min(len(s), len(t))` where `s` and `t` are the the sizes of the sets and t is a set. 
    - Finally time complexity would be `O(n)` considering n is the length of final set after appending elements to linkedlist after performing intersection on `set()`.



