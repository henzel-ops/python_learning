"""
Docstring for notes.11_arithmetic_module
"""

def add(a, b):
    """
    Add two numbers together.

    :param a: The first number.
    :param b: The second number.
    :return: The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Subtract one number from another.

    :param a: The first number.
    :param b: The second number.
    :return: The difference of a and b.
    """
    return a - b

def multiply(a, b):
    """
    Multiply two numbers together.

    :param a: The first number.
    :param b: The second number.
    :return: The product of a and b.
    """
    return a * b

print(f"This is the arithmetic module.(__name__: {__name__})")

if __name__ == "__main__":
    print("This code is running as the main program.")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"4 * 6 = {multiply(4, 6)}")