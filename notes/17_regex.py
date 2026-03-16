# Regular Expressions (regex) - re module
import re

# simple match
text = "hello world"
result = re.search(r"world", text)
print(result) #<re.Match object; span=(6, 11), match='world'>

# (match) only start of the string
result = re.match(r"world", text)
print(result) #None

# special characters Dot (.) matches any character except newline
re.search(r"h.llo", text) #<re.Match object; span=(0, 5), match='hello'>
"""
Matches
hello
hallo
hxllo
"""

# character classes
"""
Range
[0-9] - matches any digit
[a-z] - matches any lowercase letter
[A-Z] - matches any uppercase letter
[a-zA-Z] - matches any letter
[a-zA-Z0-9] - matches any alphanumeric character
"""
# range shortcuts
"""
\d - matches any digit (equivalent to [0-9])
\D - matches any non-digit character (equivalent to [^0-9])
\w - matches any alphanumeric character (equivalent to [a-zA-Z0-9_])
\W - matches any non-alphanumeric character (equivalent to [^a-zA-Z0-9_])
\s - matches any whitespace character (equivalent to [ \t\n\r\f\v])
\S - matches any non-whitespace character (equivalent to [^ \t\n\r\f\v])
"""

re.search(r"\d+", "order 1234") #<re.Match object; span=(6, 10), match='1234'>

"""
Repitition
+ - matches 1 or more
* - matches 0 or more
? - matches 0 or 1
{n} - matches exactly n times
{n,} - matches n or more times
{n,m} - matches between n and m times
"""
re.search(r"\d{3}-\d{2}-\d{4}", "SSN: 123-45-6789") #<re.Match object; span=(5, 16), match='123-45-6789'>   

"""
ANCHORS
^ - matches the start of the string
$ - matches the end of the string
\b - matches a word boundary
\B - matches a non-word boundary
"""
re.search(r"^hello", "hello world") #<re.Match object; span=(0, 5), match='hello'>
re.search(r"world$", "hello world") #<re.Match object; span=(6, 11), match='world'> 

"""
extracting data
1. findall() - returns a list of all matches
"""
re.findall(r"\d+", "item 1 costs 200 and item 2 costs 300") #[1, 200, 2, 300]

"""
2. group() - returns the matched string
3. groups() - returns a tuple of all matched groups
"""
text2 = "My email is john@example.com"
match = re.search(r"(\w+)@(\w+)\.(\w+)", text2)
print(match.group(1)) # john
print(match.group(2)) # example
print(match.group(3)) # com
print(match.groups()) # ('john', 'example', 'com')

"""
re.sub() - replaces matches with a specified string
"""
text3 = "My phone number is 9876543210"
masked = re.sub(r"\d", "*", text3)
print(masked) # My phone number is **********

"""
compile() - compiles a regex pattern for reuse
"""

pattern = re.compile(r"\d+\.\d+\.\d+\.\d+")
print(pattern.search("IP address: 192.168.1.1")) #<re.Match object; span=(12, 23), match='192.168.1.1'>