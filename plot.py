import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

data = {
    'pitch':[30, 50, 80, 20, 60, 40], # the Pith was { % } good
    'product':[50, 20, 10, 60, 70, 10], # the Product was { % } good
    'deal':[1, 0, 0, 1, 1, 0] #  1==deal | 0==noDeal

}

df = pd.DataFrame(data)

x = df[['pitch', 'product']] 
y = df['deal']

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.3, random_state=40) 

K = 4
knn = KNeighborsClassifier(n_neighbors=K)
knn.fit(xTrain, yTrain)

targerPredict = knn.predict(xTest)
accurecy = accuracy_score(yTest,targerPredict)
print(f'Acurecy::| {accurecy:.2f}')

newData = [[30, 40]]
predict = knn.predict(newData)
print(f'deal==1, noDeal==0: {predict[0]}')

plt.figure(figsize=(10, 6))
plt.scatter(xTest['pitch'], xTest['product'], c=yTest, marker='x', label='Testing Data (Actual)')
plt.scatter(newData[0][0], newData[0][1], c='black', marker='X', s=200, label='New Data Point')

plt.xlabel('PITCH')
plt.ylabel("PRODUCT")
plt.legend()
plt.colorbar(label='deal (0 = No Deal, 1 = Deal)')

plt.show()