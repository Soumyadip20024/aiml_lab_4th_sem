import pandas as pd

# Create a list containing student details: [name, height, weight, BMI status]
students_info = [
    ['Alex', 170, 65, True],   # John does not have a good BMI
    ['Warner', 160, 72, False],  # Alice does not have a good BMI
    ['Bob', 175, 70, True],    # Bob does not have a good BMI
    ['Cris', 165, 78, False] # Charlie does not have a good BMI
]

print(students_info)


# Convert the list into a Pandas DataFrame with headings
students_df = pd.DataFrame(students_info, columns=['Name', 'Height', 'Weight', 'Good_BMI'])
print("\n")
print("Convert the list into a Pandas Series:")
# Print the Pandas DataFrame
print(students_df)


