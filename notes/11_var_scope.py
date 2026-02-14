# global variable
x = 10

def my_function():
    # local variable
    x = 5
    print(f"Inside function: x = {x}") 

print(my_function())

print(f"Outside function: x = {x}")