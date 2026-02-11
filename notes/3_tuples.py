# Tuple
# A tuple is an ordered, immutable collection of elements in Python.
# Tuples are defined by enclosing elements in parentheses ().
# Tuples can contain elements of different data types, including other tuples.

t1 = ("python", 42, 3.14, True, None, [1, 2, 3], (4, 5, 6))
print(type(t1))  # Output: <class 'tuple'>
print(len(t1))   # Output: 7
print(t1)        # Output: ('python', 42, 3.14, True, None, [1, 2, 3], (4, 5, 6))   

# Accessing elements in a tuple
print(t1[0])  # Output: python
print(t1[-1]) # Output: (4, 5, 6)

t2 = 10, 20, 30, 40
print(type(t2))  # Output: <class 'tuple'>
print(t2)        # Output: (10, 20, 30, 40

t2 = tuple(t2) # converting list to tuple

# concatenation of tuples
t3 = t1 + t2
print(t3)  # Output: ('python', 42, 3.14, True, None, [1, 2, 3], (4, 5, 6), 10, 20, 30, 40)

# repetition of tuples
t4 = t2 * 2
print(t4)  # Output: (10, 20, 30, 40, 10, 20, 30, 40)   

# membership testing
print(42 in t1)  # Output: True
print(100 not in t2)  # Output: True 

# count() and index() methods
t5 = (1, 2, 3, 2, 4, 2, 5)
print(t5.count(2))  # Output: 3
print(t5.index(4))  # Output: 4
print(t5.index(2))  # Output: 1 prints the index of first occurrence of 2

# min(), max(), sum() functions
t6 = (5, 1, 9, 3, 7)    
print(min(t6))  # Output: 1
print(max(t6))  # Output: 9
print(sum(t6))  # Output: 25

# mutability immutability
# Tuples and Strings are immutable, meaning their elements cannot be changed after creation.
# Lists and Dictionaries are mutable, meaning their elements can be changed after creation.
# However, if a tuple contains a mutable element (like a list), that mutable element can be modified.

l1 = ["Mango", "Aple", "kiwi"]
print(id(t1))  # Output: some memory address
l1[-2] = "Apple"
print(l1)  # Output: ['Mango', 'Apple', 'kiwi'] cannot do this with tuple
print(id(t1))  # Output: same memory address as before (tuples are immutable)





