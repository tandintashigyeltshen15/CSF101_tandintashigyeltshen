# Documentation

# Main Concepts Applied
In this practical, I applied the concepts of data structures, specifically:
- Stack (LIFO) – Last In, First Out structure where the last element added is the first one removed.
- Queue (FIFO)** – First In, First Out structure where the first element added is the first one removed.

The implementation involved:
- Creating Python classes with methods to perform standard operations.
- Using lists as the underlying storage mechanism.
- Implementing error handling for empty structures using conditional checks.

# Reflection

# What I Learned
- How to implement abstract data structures using Python classes.
- The difference between Stack and Queue operations.
- The importance of method structure and error checking (e.g., avoiding pops from an empty stack).
- How to test and debug class-based programs.

# Challenges Faced
1. IndexError when popping/dequeuing from an empty structure 
   - Initially, I didn’t include a check before calling `.pop()`.  
   - I resolved this by adding an `if not self.is_empty()` condition before performing any removal.

2. Queue performance concern  
   - Using `pop(0)` in lists is not efficient since it shifts all elements.  
   - I learned that using `collections.deque` would be more efficient for real-world applications.

---

