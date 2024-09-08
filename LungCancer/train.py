import csv
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
import keras


# Count how many fieldnames
with open('lung1.csv') as file:
    reader = csv.reader(file)
    fieldnm = next(reader)  ## This reads and stores the header row
numFieldnm = len(fieldnm)

print(f"The CSV file has {numFieldnm} fieldnames (columns).")



# Load data from the CSV file
with open('lung1.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header

    data = []
    for row in reader:
        data.append({
            'evidence': [int(cell) for cell in row[1:15]],  # Adjust range to match the 14 features
            'label': 1 if row[15] == '1' else 0
        })

evidence = np.array([row['evidence'] for row in data])
label = np.array([row['label'] for row in data])

print(f"Number of samples: {len(evidence)}")

# Check if dataset is empty
if len(evidence) == 0:
    raise ValueError("The dataset is empty. Please check the data loading process.")

testSize = 0.2
xTrain, xTest, yTrain, yTest = train_test_split(
    evidence, label, test_size=testSize
)


# Check sizes of training and testing sets
print(f"\n\n\nTraining set size: {len(xTrain)}")
print(f"Testing set size: {len(xTest)}\n\n\n")

#build the neural network model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(8, input_shape=(14,), activation='relu'))  
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

# Compile the model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',  
    metrics=['accuracy']
)


model.fit(xTrain, yTrain, epochs=15)

model.evaluate(xTest, yTest, verbose=2)#Displays one line per epoch with detailed information such as loss and accuracy without a progress bar.


# New test data (Example: GENDER, AGE, SMOKING, ..., CHEST PAIN)
new_data = np.array([[1, 69, 1, 2, 2, 1, 1, 2, 1, 2, 2, 2, 2, 2]])  # Replace with actual test data

new_data = new_data.reshape(1, 14)

# Predict the label (probability of class 1)
prediction = model.predict(new_data)

# Convert probability to binary class (0 or 1)
predicted_class = 1 if prediction >= 0.5 else 0

# Output the result
print(f"Predicted class: {predicted_class}")
