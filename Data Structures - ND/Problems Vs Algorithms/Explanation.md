#  Problem 1 - Floored square root
## Approach
Since the problem statement required an `O(log n)` solution, I used the same approach used for Binary search by dividing the number by half until either of the divided value or its `+1` of the current value are in the boundaries of the given number
## Efficiency
#### Time Complexity
As specified the time complexity would be `O(log n)` it follows the same principle of binary search which is decrease and conquer.
#### Space Complexity
The space complexity is O(1). No additional space is required to execute this algorithm.

# Problem 2 - Rotated array search
## Approach
- I have used binary search algorithm with slight modification by maintaining `low`, `high` and `mid`. 
- It constantly finds the mid for every itertion and checks if the elements at low and high are in order or else it updates low and high until it finds the right sub array to perform binary search for the given number. 
- Time complexity for binary search is `O(Log n)` because of our dividing on each iteration of `O(n)`
## Efficiency
#### Time Complexity
Therefore this is same as binary search essentially diving the array in half iteratively so the overall time complexity would be `O(n log n)`
#### Space Complexity
The space complexity is `O(log(n))`. The input_list gets split into 2.


# Problem 3 - Rearrange array digits
## Approach
Since the problem statement required an `O(n log n)` solution, I used quick sort for sorting the list and then used two variables to store number from the sorted list in alternating sequence in decreasing order so that the final combination provides maximum sum
## Efficiency
#### Time Complexity
As specified the time complexity would be `O(n log n)` as it uses quick sort which has time complexity of `O(n log n)` . Main code runs in `O(n)` and sort in `O(n log n)`. We consider more dominant Big - O notation which is `O(n log n)` as `O(n log n)>O(n)`. Finally time complexity would be `O(n log n)`
#### Space Complexity
This algorithm has a space complexity of `O(n)`, as it is just re-arranging the input array in place.

# Problem 4 - Dutch National Flag
## Approach
The problem solution was directly given in the course materials, so I really just pasted it from there. Of course I made sure to understand it properly.
## Efficiency
#### Time Complexity
The time complexity of this algorithm is `O(n)`, using just a single traversal. 
#### Space Complexity
The space complexity is again `O(1)`, as this algorithm is just re-arranging the given array in place.


# Problem 5 - Autocomplete with Tries
## Approach
I used trie implementation as suggested by storing each character in dictionary with it's sub-sequent characters as it's childern and also storing a flag variable `isWord` which would indicate if it's a word or not.  `find()` helps us retrieving  particular node in sequence then `suffixes()` would eventually recursively traverse from the current node to all possible paths recursively and returning the remaining letters in all possible words
## Efficiency
#### Time Complexity
- The main algorithm is `suffixes()` which is very similar to `find_files` from the previous section. Each node is only inspected once, but extending the list as opposed to appending to it is relatively expensive. 
- Therefore, its time complexity ends up `O(n*m)` `n` represents number of characters in prefix and `m` represents average number of child nodes.
#### Space Complexity
The space complexity for the data structure is `O(n*m)`, where `n` is the number of words stored in the trie, and `m` the longest word length. 

# Problem 6 - Unsorted Integer Array
## Approach
This was pretty straightforward to have to varaibles `min` and `max` which will be updated while iterating the list.
## Efficiency
#### Time complexity
Time complexity will be `O(n)` because of our loop iteration over `n` elements
#### Space complexity 
The space complexity is `O(1)`. The algorithm only uses a few fixed auxiliary variables.


# Problem 7 - Routing with Tries
## Approach
This was again similar to auto complete with just a little tweaks needed. Instead of character I used words as dict keys and instead of `isWord` I used `handler` to check if there is any handler assigned. `split_path()` was basically extracting words from the path and parsing it to the `insert()` to create the dictionary.
## Efficiency
#### Time Complexity
The most interesting algorithm is probably `lookup()`. `split_path()` is `O(n)`, and the find algorithm is something like `O(n*k)`, where  `n`  is the longest path and  `k`  the average number of branches: It has to iterate through the trie nodes (worst case the longest path), and at each level find the next path element out of all branches. So the overall time complexity is `O(n*k)` as it's more dominant factor. 
#### Space Complexity
The space complexity is `O(n*m)`, where `n` is the number of paths stored in the trie, and `m` the longest path length.
