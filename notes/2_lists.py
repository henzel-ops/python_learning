name = "john"
age = 20
percent = 85.5

student = [name, age, percent]

print(type(student)) # Output: <class 'list'>
print(student)  # Output: ['john', 20, 85.5]

days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print(days_of_week[0]) # Output: Mon first item
print(days_of_week[-1]) # Output: Sun last item

# length of a list => the number of items/elements in the list
print(len(days_of_week))

# slicing lists same as slicing strings
l1 = [3, 8, 1, 0, 4, 9, 7, 3, 6]
print(l1[1:6:1]) # will print [8, 1, 0, 4, 9] it wont print the last [6] index
print(l1[2:7:2]) # will print [1, 4, 7] wont print the last index

# concatination of lists
l2 = [1, 7, 2]
l3 = [0, 5]

print(l2 + l3) # it extends the list [1, 7, 2, 0, 5]

# Repition of lists
print(l3 * 3) # repeats 3 times [0, 5, 0, 5, 0, 5]

# list methods
# append()
# adds an item to the end of the list

fruits = ["Mango", "Apple", "Orange"]
print(fruits)

# append adds only one ele at a time
print(fruits.append("banana")) # returns None bc it adds to the end of fruits list

print(fruits) # banana gets added to end of the list

"""
# insert
syntax: list.insert(index, item)
"""
fruits.insert(2, "kiwi")
print(fruits)

"""
extend() we give list of values instead of comma separated values
remove()
pop()
"""
fruits.extend(["grapes", "pear"])
print(fruits)   # Output: ['Mango', 'Apple', 'kiwi', 'Orange', 'banana', 'grapes', 'pear']
fruits.append(["watermelon", "pineapple"])
print(fruits)   # Output: ['Mango', 'Apple', 'kiwi', 'Orange', 'banana', 'grapes', 'pear', ['watermelon', 'pineapple']]

fruits.remove("kiwi")
print(fruits)   # Output: ['Mango', 'Apple', 'Orange', 'banana', 'grapes', 'pear', ['watermelon', 'pineapple']]

# repeated value remove's only first occurence
fruits.append("Apple")  
fruits.remove("Apple")
print(fruits)   # Output: ['Mango', 'Orange', 'banana', 'grapes', 'pear', ['watermelon', 'pineapple'], 'Apple']

# pop removes last item if index not provided
fruits.pop(-2)
print(fruits)   # Output: ['Mango', 'Orange', 'banana', 'grapes', 'pear', 'Apple']

"""
reverse() - reverses the list in place
sort() - sorts the list in ascending order  
count() - returns the number of occurrences of an element in the list
membership - in, not in
"""
days_of_week.reverse()
print(days_of_week)   # Output: ['Sun', 'Sat', 'Fri', 'Thu', 'Wed', 'Tue', 'Mon']

nums = [6, 5, 2, 9, 1, 5, 6]
nums.sort()
print(nums)   # OUTPUT: [1, 2, 5, 5, 6, 6, 9]

nums.sort(reverse=True)
print(nums)   # OUPUT: [9, 6, 6, 5, 5, 2, 1]

occurrences = nums.count(6)
print(occurrences)   # OUTPUT: 2

languages = ["Python", "Java", "C++", "JavaScript"]
print("Java" in languages)  # Output: True
print("Ruby" not in languages)  # Output: True

"""
min() - returns the smallest item in the list
max() - returns the largest item in the list
sum() - returns the sum of all items in the list
"""

numbers = [10, 3, 7, 1, 9]
print(min(numbers))  # Output: 1
print(max(numbers))  # Output: 10
print(sum(numbers))  # Output: 30

# nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])  # Output: [1, 2, 3]
print(matrix[1][2])  # Output: 6

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12, [2, 4, 6]]
]

print(matrix1[3][3][1])  # Output: 4


