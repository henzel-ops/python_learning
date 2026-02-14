import random

fruits = ['apple', 'banana', 'cherry', 'date']
random_fruit = random.choice(fruits)
print(f"Randomly selected fruit: {random_fruit}")

random_number = random.randint(1, 100)
print(f"Randomly selected number between 1 and 100: {random_number}")

random_float = random.uniform(1.0, 10.0)
print(f"Randomly selected float between 1.0 and 10.0: {random_float}")

random.shuffle(fruits)
print(f"Shuffled fruits list: {fruits}")

random2 = random.random()
print(f"Random float between 0.0 and 1.0: {random2}")

