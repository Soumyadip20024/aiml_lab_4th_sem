# Logistic Regression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

import numpy as np

# Step 1: Load your dataset
data = pd.read_csv('logistic_reg.csv')

# Step 2: Preprocess the dataset
X = data[['Score']]

# Target: 'Accepted'
y = data['Accepted']

# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 4: Initialize the logistic regression model
model = LogisticRegression()

# Step 5: Train the model
model.fit(X_train, y_train)

# Step 6: Predict on the test set
y_pred = model.predict(X_test)

# Step 7: Evaluate the model
# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Step 8: Plotting the Logistic Regression Curve
plt.figure(figsize=(8, 6))

# Scatter plot of the data points
plt.scatter(X['Score'], y, color='blue', label='Data points')

# Plot the logistic regression curve
# Generate a range of values from the min to max of X for smooth curve
z = np.linspace(X['Score'].min(), X['Score'].max(), 300)

p = model.predict_proba(z.reshape(-1, 1))[:, 1]  # Get the probability for the positive class
plt.plot(z, p, color='red', label='Logistic Regression Curve')

# Adding titles and labels
plt.title('Logistic Regression Curve')
plt.xlabel('Score')
plt.ylabel('Probability of Accepted')
plt.legend()
# Show plot

plt.grid(True)
plt.show()
# Classification Report

print("Classification Report:")
print(classification_report(y_test, y_pred))