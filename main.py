# Create an empty list
my_list = []

# Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert 15 at index 1 (second position)
my_list.insert(1, 15)

# Extend the list with multiple elements
my_list.extend([50, 60, 70])

# Remove the last element (70)
my_list.pop(-1)

# Sort the list in ascending order
my_list.sort()

# Find the index of the value 30
index_30 = my_list.index(30)

# Print the index of 30
print(index_30)  # Output: 3