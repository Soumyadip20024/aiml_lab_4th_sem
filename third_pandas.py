import pandas as pd
import numpy as np


weights = pd.Series(np.random.randint(45, 61, size=30))


item_at_index_3 = weights[3]  
print("Item at index 3:", item_at_index_3)

# Retrieve a range of items using slicing (for example, index 2 to 5)
items_from_index_2_to_5 = weights[2:6]  # This retrieves items from index 2 to 5 (excluding index 6)
print("Items from index 2 to 5:", items_from_index_2_to_5)

print("\n")
# Retrieve items from index 17 to 27 (inclusive of 17, exclusive of 28)
items_from_index_17_to_27 = weights[17:28]

# Print the items
print("Items from index 17 to 27:", items_from_index_17_to_27)


print("\n")

# Compute the modal value in the 'weights' series
modal_value = weights.mode()

# Print the modal value
print("The modal value(s) in the series:", modal_value)

print("\n")

# Sort the values in the 'weights' series in increasing order
sorted_weights = weights.sort_values()

# Print the sorted values
print("Weights in increasing order:")
print(sorted_weights)

print("\n")

# Sort the values in the 'weights' series in decreasing order
sorted_weights_desc = weights.sort_values(ascending=False)

# Print the sorted values in decreasing order
print("Weights in decreasing order:")
print(sorted_weights_desc)

print("\n")

# Count the number of times each item occurs in the 'weights' series
value_counts = weights.value_counts()

# Print the counts
print("Number of times each item occurs:")
print(value_counts)
