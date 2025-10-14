# Documentation

# Main Concepts Applied
In this practical, I implemented and explored Linked Lists, a fundamental dynamic data structure.  
The key concepts used were:
- Nodes and pointers – each node contains data and a reference to the next node.
- Dynamic memory allocation – unlike arrays, linked lists grow and shrink at runtime.
- Pointer manipulation – updating node links to reverse, merge, and remove nodes efficiently.
- Two-pointer approach – used in both reversing and removing the Nth node from the end.

# Reflection

# What I Learned
- How to create and traverse a linked list using custom `Node` and `LinkedList` classes.
- How to manipulate pointers to reverse a list without extra memory.
- How to merge two sorted linked lists using iteration and dummy nodes.
- How to remove the Nth node from the end using two pointers efficiently.
- The importance of edge cases (e.g., empty lists, single-element lists).

---

# Challenges Faced
1. Infinite Loop During Reversal  
   - Initially forgot to move `current = next_node` inside the loop.  
   - Fixed it by correctly updating the traversal pointer.

2. Removing the Wrong Node  
   - Miscalculated the offset between fast and slow pointers in `removeNthFromEnd`.  
   - Resolved it by adding an extra dummy node to handle edge cases like deleting the head node.

3. Testing Merge Function* 
   - Encountered issues when one list was empty.  
   - Solved by adding final checks:  
     ```python
     if list1: current.next = list1
     if list2: current.next = list2
     ```

# Conclusion
This practical deepened my understanding of linked data structures and pointer-based algorithms.  
It helped me improve logical problem-solving and debugging skills, especially in handling edge cases and pointer manipulation in Python.
