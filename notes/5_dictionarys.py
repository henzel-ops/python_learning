# about dictionarys in python
# A dictionary is an unordered, mutable collection of key-value pairs in Python.where each key is unique.
# Dictionaries are defined by enclosing key-value pairs in curly braces {key: value}.

# Creating a dictionary
student = {
    "name": "John Doe",
    "age": 21,
    "courses": ["Math", "Science", "History"],
    "is_active": True
}
print(type(student))  # Output: <class 'dict'>
print(len(student))   # Output: 4
print(student)        # Output: {'name': 'John Doe', 'age': 21, 'courses': ['Math', 'Science', 'History'], 'is_active': True}

# Accessing values in a dictionary using keys
print(student["name"])      # Output: John Doe
print(student.get("age"))   # Output: 21    
print(student["courses"])   # Output: ['Math', 'Science', 'History']
# print(student["grade"])    # Raises KeyError
print(student.get("grade", "Not Found"))  # Output: Not Found or default value None 

# Adding or updating key-value pairs
student["grade"] = "A"
print(student)  # Output: {'name': 'John Doe', 'age': 21, 'courses': ['Math', 'Science', 'History'], 'is_active': True, 'grade': 'A'}
student["age"] = 22  # Update age
print(student)  # Output: {'name': 'John Doe', 'age': 22, 'courses': ['Math', 'Science', 'History'], 'is_active': True, 'grade': 'A'}
student.update({"is_active": False, "graduation_year": 2023}) # Update multiple key-value pairs

#membership testing
print("name" in student)      # Output: True
print("address" not in student)  # Output: True 

# Removing key-value pairs
removed_value = student.pop("grade")  # Removes 'grade' key and returns its value
print(removed_value)  # Output: A
print(student)  # Output: {'name': 'John Doe', 'age': 22, 'courses': ['Math', 'Science', 'History'], 'is_active': False, 'graduation_year': 2023}

groceries = {'milk': 2, 'bread': 1, 'eggs': 12, 'apples': 6, 'milk': 3} # duplicate key milk will keep the last value because it reads from left to right
print(groceries)  # Output: {'milk': 3, 'bread': 1, 'eggs': 12, 'apples': 6}

# Dictionary methods
keys = student.keys()
print(keys)  # Output: dict_keys(['name', 'age', 'courses', 'is_active', 'graduation_year'])
values = student.values()
print(values)  # Output: dict_values(['John Doe', 22, ['Math', 'Science', 'History'], False, 2023])
items = student.items()
print(items)  # Output: dict_items([('name', 'John Doe'), ('age', 22), ('courses', ['Math', 'Science', 'History']), ('is_active', False), ('graduation_year', 2023)])

# what can be used as keys in dictionary
# keys must be immutable types like strings, booleans, numbers, or tuples (if the tuple contains only immutable elements)
# lists or other dictionaries cannot be used as keys because they are mutable
valid_dict = {
    "string_key": "value1",
    42: "value2",
    (1, 2): "value3"
}

print(valid_dict)  # Output: {'string_key': 'value1', 42: 'value2', (1, 2): 'value3'}
# invalid_dict = {
#     [1, 2]: "value4",  # Raises TypeError
#     {"key": "value"}: "value5"  # Raises TypeError
# }
# print(invalid_dict)  # Output: TypeError: unhashable type: 'list'

