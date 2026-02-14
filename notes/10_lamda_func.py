def add(a, b):
    return a + b

lambda_add = lambda a,b: a + b

res = lambda_add(1,2)

print(res)

# lambda with filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = list(filter(lambda x : x % 2 != 0, numbers))

print(odd_numbers) # Output: [1, 3, 5, 7, 9]

# lambda with map
squared_numbers = list(map(lambda x : x ** 2, numbers))
print(squared_numbers) # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
