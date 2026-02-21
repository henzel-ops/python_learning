# about json and pickle modules
import json
import pickle

# JSON
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

data1 = {'student1': {'name': 'Alice', 'age': 30, 'city': 'New York'},
         'student2': {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
         'student3': {'name': 'Charlie', 'age': 35, 'city': 'Chicago'},
         'student4': {'name': 'David', 'age': 25, 'city': 'Houston'},
            }

# Serialize to JSON in a file
with open('notes/data.json', 'w') as f:
    json.dump(data, f, indent=4)

# Deserialize from JSON file
with open('notes/data.json', 'r') as f:
    loaded_data = json.load(f)
print('Loaded JSON data: ', loaded_data)

# update JSON data
loaded_data['age'] = 31
with open('notes/data.json', 'w') as f:
    json.dump(loaded_data, f, indent=4)

# using json.update() 
with open('notes/data.json', 'r') as f:
    data = json.load(f)
data.update({'age': 32})
with open('notes/data.json', 'w') as f:
    json.dump(data, f, indent=4)

# print updated data
with open('notes/data.json', 'r') as f:
    updated_data = json.load(f)
print('Updated JSON data: ', updated_data)

# Pickle
# Serialize to pickle file
with open('notes/data.bin', 'wb') as f:
    for key in data1:
        print('Pickling data for: ', key)
        pickle.dump(data1[key], f)

# Deserialize from pickle file
with open('notes/data.bin', 'rb') as f:
    #   while loop to read multiple objects from the file
    while True:
        try:
            loaded_data1 = pickle.load(f)
            if loaded_data1['age'] == 25:
                print('Loaded Pickle data for age 25: ', loaded_data1)
            #print('Loaded Pickle data: ', loaded_data1)
        except EOFError:
            print('End of file reached')
            break

