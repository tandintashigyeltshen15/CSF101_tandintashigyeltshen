# Documentation
In this practical, I implemented three types of search algorithms:

1. Linear Search
Sequentially checks each element in the list until the target is found or the list ends.
Works on unsorted lists.
Time complexity: O(n).

2. Binary Search (Iterative)
Works only on sorted lists.
Repeatedly divides the search range in half and compares the middle element to the target.
Time complexity: O(log n).

3. Binary Search (Recursive)
Same logic as iterative binary search but implemented using recursion.
Recursively searches either the left or right half of the array.
Time complexity: O(log n), with extra space due to recursive call stack.

# Reflection
What I Learned:
Linear search is simple but inefficient for large datasets.
Binary search is much faster than linear search for sorted data.
Recursion can simplify the implementation of binary search and improve readability.
The importance of sorting data before applying binary search.
How to handle cases where the target is not present using return values like -1.

# Challenges Faced and Solutions

1. Binary search on an unsorted list
Initially tried binary search on an unsorted array and got wrong results.
Solution: Always sort the array before performing binary search.

2. Recursive function errors
Forgetting the base case (left > right) caused infinite recursion in some tests.
Solution: Added proper base condition to terminate recursion.

3. Confusing indexes between sorted and original lists
When testing with a sorted array, the index returned didn’t match the original list.
Solution: Clarified that binary search returns the index in the sorted list, not the original array.

# Conclusion
This practical helped me understand the strengths and limitations of different search algorithms.
I learned that linear search is straightforward but slow for large datasets, while binary search is efficient but requires sorted data.
Additionally, recursion can make certain algorithms more elegant, but careful handling of base cases is essential to avoid errors.

Overall, this exercise improved my problem-solving skills and my understanding of search algorithms, both iterative and recursive.