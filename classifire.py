import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = {
    'humidity':[80, 85, 90, 60, 55], # humidity levels ( % ) 
    'pressur':[1005, 1010, 1030, 980, 940], # air pressure hectopascals (hPa)
    'rain':[1, 1, 1, 0, 0] # rain==1, noRain==0
}

df = pd.DataFrame(data)
print(f'DataFrame:\n{df}')


X = df[['humidity', 'pressur']] # inputData
y = df['rain'] # target or prediction

# Split the data into training and testing sets
xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size=0.3, random_state=40)

# Initialize and train the Decision Tree classifier
classifier = DecisionTreeClassifier()
classifier.fit(xTrain, yTrain)

yPrediction = classifier.predict(xTest)

accuracy = accuracy_score(yTest, yPrediction)
print(f'Accuracy: {accuracy:.2f}')

#  making a new prediction
newData = [[70, 980]]  #  Humidity 80%, Pressure 980 hPa
predict = classifier.predict(newData)
print(f'rain==1, noRain==0: {predict[0]}') 