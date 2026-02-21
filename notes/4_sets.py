# set are non sequential and unordered collection of unique items cannot be indexed
# sets are mutable meaning we can add or remove items after creation
# unique values only no duplicates allowed
# items are enclosed in curly braces {} and are separated by commas
# cannot be sliced or indexed like lists or tuples

set1 = {10, "Python", 2.5}
print(type(set1))  # Output: <class 'set'>
print(len(set1))   # Output: 3
print(set1)        # Output: {10, 'Python', 2.5}    


set2 = {10, 20, 30, 10, 20}
print(set2, type(set2))  # Output: {10, 20, 30} <class 'set'> duplicates removed

# membership testing
print(20 in set2)  # Output: True
print(50 not in set2)  # Output: True

# type casting to set
list1 = [1, 2, 2, 3, 4, 4, 5]
set_from_list = set(list1)
print(set_from_list)  # Output: {1, 2, 3, 4, 5} duplicates removed

"""
does not support concatenation or repetition operations
set1 + set2  # raises TypeError
set1 * 3     # raises TypeError"""
# sets are mutable
set2.add(40) # if duplicate value is ignored
print(set2)  # Output: {10, 20, 30, 40} 
set2.remove(20)
print(set2)  # Output: {10, 30, 40} 
# discard does not raise error if item not found
set2.discard(50)
print(set2)  # Output: {10, 30, 40} does not raise error

# set logical operations
students1 = {"English", "Maths", "cs", "Physics", "Chemistry"}
student2 = {"Biology", "English", "Chemistry", "Physics"}
student3 = {"History", "Geography"}

# common subjects in both sets
common_subjects = students1.intersection(student2)
print(common_subjects)  # Output: {'English', 'Chemistry', 'Physics'}

common_subjects = students1 & student2
print(common_subjects)  # Output: {'English', 'Chemistry', 'Physics'}

# all subjects from both sets
all_subjects = students1.union(student2, student3)
print(all_subjects)  # Output: {'Maths', 'cs', 'Biology', 'Chemistry', 'English', 'Physics', 'History', 'Geography'}
all_subjects = students1 | student2 | student3
print(all_subjects)  # Output: {'Maths', 'cs', 'Biology', 'Chemistry', 'English', 'Physics', 'History', 'Geography'}

# difference between two sets
unique_subjects = students1.difference(student2)
print(unique_subjects)  # Output: {'Maths', 'cs'}
unique_subjects = students1 - student2
print(unique_subjects)  # Output: {'Maths', 'cs'}
# symmetric difference - subjects in either set but not in both

# frozen sets - immutable version of set
frozen_set1 = frozenset([1, 2, 3, 4, 5])
print(type(frozen_set1))  # Output: <class 'frozenset'>
print(frozen_set1)        # Output: frozenset({1, 2, 3, 4, 5})

# can perform set operations but cannot add or remove items
frozen_set2 = frozenset([4, 5, 6, 7, 8])
common_items = frozen_set1.intersection(frozen_set2)
print(common_items)  # Output: frozenset({4, 5})        
all_items = frozen_set1.union(frozen_set2)
print(all_items)  # Output: frozenset({1, 2, 3, 4, 5, 6, 7, 8})
# frozen_set1.add(10)  # raises AttributeError
# frozen_set2.remove(4)  # raises AttributeError   
