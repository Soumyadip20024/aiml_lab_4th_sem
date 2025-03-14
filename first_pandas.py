
import pandas as pd
import numpy as np


weights = pd.Series(np.random.randint(45, 61, size=30))

# Print the series
#print(weights)

#print(type(weights))

rows = weights.shape[0]
columns = 1  


print("Number of rows:", rows)
print("Number of columns:", columns)

print("\n")
average_value = weights.mean()


print("The average value is:", average_value)


print("\n")
min_value = weights.min()
max_value = weights.max()

# Print the results
print("The maximum value is:", max_value)
print("The minimum value is:", min_value)

print("\n")

print("weight of first 5 elements")
print(weights.head(5))

print("\n")
print("weight of last 5 elements")
print(weights.tail(5))

print("\n")

