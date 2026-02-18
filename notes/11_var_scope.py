# global variable
x = 10

def my_function():
    # local variable
    x = 5
    print(f"Inside function: x = {x}") # x=5, local var shadows global var 

print(my_function())

print(f"Outside function: x = {x}") # x=10, global var is not affected by local var

# accessing global var within func
def access_global():
    global x
    print(f"Inside function after modifying global x: x = {x}")

access_global() # x=10 