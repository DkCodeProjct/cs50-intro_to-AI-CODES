import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

data = {
    'hardWork':[50, 20, 80, 40, 70, 60],
    'randomChance':[20, 30, 10, 5, 3, 2],
    'success':[1, 0, 1, 0, 1, 1]
}

df = pd.DataFrame(data)
print(f'DataFrame:\n{df}')
X = df[['hardWork', 'randomChance']]

y = df['success']

xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size=0.3 ,random_state=40)

classifire = DecisionTreeClassifier()
classifire.fit(xTrain, yTrain)

successPredict = classifire.predict(xTest) 

accurecy = accuracy_score(yTest ,successPredict)
print(f'Accurecy: {accurecy:.2f}')

newData = [[50, 50]]
prediction = classifire.predict(newData)

print(f'Prediction:{"success" if prediction[0] == 1 else "noSuccess"}')