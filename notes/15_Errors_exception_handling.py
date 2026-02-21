# about try except else finally

try:
    fh = open('notes/test.txt', 'r+')
    fh.write('This is a test file')
except FileNotFoundError as e:
    print('File not found error: ', e)
except Exception as e:
    print('An error occurred: ', e)
else:
    print('File opened successfully')

    fh.seek(0)  # Move the file pointer back to the beginning of the file
finally:
    print(fh.read())

try:    
    fh.close()
except Exception as e:
    print('An error occurred while closing the file: ', e)

# raise an exception
def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b    

try:
    result = divide(10, 0)
except ValueError as e:
    print('Value error: ', e)
else:
    print('Result: ', result)   