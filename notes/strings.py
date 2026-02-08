# About Strings 

s1 = "Hello World"
print(s1)  # Output: Hello World

# get length of string
print(len(s1))  # Output: 11

# indexing
print(s1[0])  # Output: H first character
print(s1[-1])  # Output: W last character

"""
# Slicing
# indexing for single character
# slicing for range of characters
# list_slicing[start: end: step]

- start : starting index at which slicing operation starts (default is 0)
- end : ending index at which the slicing operation stops (default is length of string) (excluded)
- step : integer that specifies the increment between each index for slicing (default is 1)
"""
print(s1[2:7:1]) # Output: llo W characters from index 2 to 6

print(s1[2:9:2]) # Output: loWr characters from index 2 to 8 with step 2

slices1 = s1[1:12:3]
print(slices1) # Output: eood characters from index 1 to 11 with step 3

print(type(slices1)) # Output: <class 'str'>

# Reverse a string using slicing
rev_s1 = s1[::-1]
print(rev_s1)  # Output: dlroW olleH

# f-strings (formatted string literals) instead of normal placeholder formatting
name = "Alice"
age = 30

greeting = f"My name is {name} and I am {age} years old."
print(greeting)  # Output: My name is Alice and I am 30 years old

"""
Escape Characters
- \n : new line
- \t : tab
- \\ : backslash
- \' : single quote
- \" : double quote 
"""

print("Hello\nWorld")  # Output: Hello (new line) World
print("Hello\tWorld")  # Output: Hello (tab) World
print("This is a backslash: \\")  # Output: This is a backslash: \
print('She said, "Hello!"')  # Output: She said, "Hello!"
print('It\'s a nice day!')  # Output: It's a nice day!

# String operations

s2 = "Python"
version = "3.9"

# Concatenation
full_string = s2 + " " + version
print(full_string)  # Output: Python 3.9

# Repetition
repeated_string = s2 * 3
print(repeated_string)  # Output: PythonPythonPython

# Membership
# in
print("P" in s2)  # Output: True
print("p" in s2)  # Output: False (case-sensitive)

# not in
print("x" not in s2)  # Output: True
print("o" not in s2)  # Output: False (o is in Python

# comparison of strings
print("abc" == "abc")  # Output: True
print("abc" == "ABC")  # Output: False (case-sensitive)
print("abc" != "def")  # Output: True
print("abc" < "abd")  # Output: True (lexicographical order)
print("abc" > "abb")  # Output: True (lexicographical order)

# String methods    
s3 = "  Hello World  "  
print(s3.strip())  # Output: Hello World (removes leading and trailing whitespace)
print(s3.upper())  # Output:   HELLO WORLD   (converts to uppercase)
print(s3.lower())  # Output:   hello world   (converts to lowercase)
print(s3.replace(" ", "_", 1))  # Output: _Hello World  (replaces first space with underscore)
print(s3.split())  # Output: ['Hello', 'World'] (splits the string into a list of words)    
print(s3.title()) # Output:   Hello World   (converts to title case)
print(s3.capitalize()) # Output:   hello world    (capitalizes the first character of the string)
print(s3.startswith("  He"))  # Output: True (checks if the string starts with "  He")
print(s3.endswith("ld  "))  # Output: True (checks if the string ends with "ld  ")


# Counting occurrences of a substring
s4 = "banana"
print(s4.count("a"))  # Output: 3 (counts the number of 'a' in the string)
