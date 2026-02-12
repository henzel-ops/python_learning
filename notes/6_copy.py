import copy

# Shallow Copy
og_list = [1, 2, [3, 4], 5]
shallow_list = copy.copy(og_list)
print("Original List:", og_list)          # Output: [1, 2, [3, 4], 5]
print("Shallow Copied List:", shallow_list)  # Output: [1, 2, [3, 4], 5]

# Modifying the nested list in the shallow copy
shallow_list[2][0] = 'Changed'
print("After modifying shallow copy:")
print("Original List:", og_list, "id:", id(og_list[2]))          # Output: [1, 2, ['Changed', 4], 5]
print("Shallow Copied List:", shallow_list, "id:", id(shallow_list[2]))  # Output: [1, 2, ['Changed', 4], 5]
print(f"first layer id same? {id(og_list) == id(shallow_list)}")  # False
print(f"second layer id same? {id(og_list[2]) == id(shallow_list[2])}")  # True

# Deep Copy
og_list2 = [1, 2, [3, 4], 5]
deep_list = copy.deepcopy(og_list2)
print("\nOriginal List 2:", og_list2)          # Output: [1, 2, [3, 4], 5]
print("Deep Copied List:", deep_list)  # Output: [1, 2, [3, 4], 5]
# Modifying the nested list in the deep copy
deep_list[2][0] = 'ChangedDeep'
print("After modifying deep copy:")
print("Original List 2:", og_list2, "id:", id(og_list2[2]))          # Output: [1, 2, [3, 4], 5]
print("Deep Copied List:", deep_list, "id:", id(deep_list[2]))  # Output: [1, 2, ['ChangedDeep', 4], 5]
print(f"first layer id same? {id(og_list2) == id(deep_list)}")  # False
print(f"second layer id same? {id(og_list2[2]) == id(deep_list[2])}")  # False