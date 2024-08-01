import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

data = {
    'age':[22, 28, 30, 55, 45, 42],
    'bmi':[20, 20, 22, 25, 28, 22],
    'sugarLvl':[0, 0, 0, 1, 1, 0 ]
}

df = pd.DataFrame(data)
print(f'Data Frame :::\n{df}')
x = df[['age', 'bmi']] # input's

y = df['sugarLvl'] # targert

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.3, random_state=40)

K = 3

kClasifir = KNeighborsClassifier(n_neighbors=K)
kClasifir.fit(xTrain, yTrain)

targertPredict = kClasifir.predict(xTest)

accurecy = accuracy_score(yTest,targertPredict)
print(f'Acurecy: {accurecy:.2f}')

newData = [[40, 18]]
predict = kClasifir.predict(newData)
print(f'sugar==1, noSugar==0: {predict[0]}')
