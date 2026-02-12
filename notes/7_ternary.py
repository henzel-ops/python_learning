num = int(input("Enter a number: "))
"""
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
"""
# Using ternary operator

# syntax: [on_true] if [condition] else [on_false]
print("Even") if num % 2 == 0 else print("Odd")