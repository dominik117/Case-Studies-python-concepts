# BASIC SLICING
print("BASIC SLICING")

# Define a list for demonstration
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing format: list[start:stop:step]
# Extracts a portion of a list from 'start' to 'stop' - 1, with 'step' increments

# Slicing from index 2 to 5 (not including 5)
slice1 = my_list[2:5]  # [2, 3, 4]

# Slicing from the beginning to index 5 (not including 5)
slice2 = my_list[:5]  # [0, 1, 2, 3, 4]

# Slicing from index 3 to the end of the list
slice3 = my_list[3:]  # [3, 4, 5, 6, 7, 8, 9]

# Slicing with a step (every second element from the entire list)
slice4 = my_list[::2]  # [0, 2, 4, 6, 8]

# Printing results
print("Basic Slices:", slice1, slice2, slice3, slice4)

# NEGATIVE INDEXING AND STEPS
print("NEGATIVE INDEXING AND STEPS")

# Negative indices count from the end of the list

# Slicing from the third-last to the last element
slice1 = my_list[-3:]  # [7, 8, 9]

# Slicing with a negative step (reverses the list)
slice2 = my_list[::-1]  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Combining negative indices and steps
slice3 = my_list[-3:-6:-1]  # [7, 6, 5]

# Printing results
print("Negative Indexing and Steps:", slice1, slice2, slice3)


# EDGE CASES
print("EDGE CASES")
# Slicing beyond list boundaries is handled gracefully in Python

# Slicing beyond the end
slice1 = my_list[10:15]  # Returns an empty list []

# Slicing with a step that skips entire list
slice2 = my_list[::100]  # Returns the first element [0]

# Printing results
print("Edge Cases:", slice1, slice2)

