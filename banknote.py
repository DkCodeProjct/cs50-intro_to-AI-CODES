import random
import csv

from sklearn.linear_model import Perceptron
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.naive_bayes import GaussianNB
#from sklearn.svm import SVC


class BankNoteAuthenticator:
    def __init__(self, filename):
        self.filename = filename
        self.data = []
        self.model = Perceptron()
        #sellf.model = KNeighborsClassifier()
        #sellf.model = SVC()

    def loadData(self):
        with open(self.filename) as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                self.data.append({
                    'evidence':[float(cell) for cell in row[4:]], # all Rows eccept Class 4:
                    'label': 'genuine' if int(row[4]) == 0 else 'counterfiet'
                })

    
    def splitData(self, testSize=0.4):
        holt = int(testSize * len(self.data))
        random.shuffle(self.data)
        self.testingData = self.data[:holt]
        self.trainingData = self.data[holt:]
    
    def training(self):
        xTraining = [row['evidence'] for row in self.trainingData]
        yTraning = [row['label'] for row in self.trainingData]
        self.model.fit(xTraining, yTraning)
    
    def evaluate(self):
        xTesting = [row['evidence'] for row in self.testingData]
        yTesting = [row['label'] for row in self.testingData]
        predictions = self.model.predict(xTesting)

        correct = 0
        incorrect = 0
        total = len(yTesting)

        for acual, predict in zip(yTesting, predictions):
            if acual == predict:
                correct += 1
            else:
                incorrect += 1
        
        accuracy = 100 * correct / total
        print(f'Result for {type(self.model).__name__}')
        print(f'Correct: {correct}')
        print(f'Incorrect: {incorrect}')
        print(f'Accuracy: {accuracy:.2f}%')

authenticator = BankNoteAuthenticator('banknotes.csv')
authenticator.loadData()
authenticator.splitData(testSize=0.4)
authenticator.training()
authenticator.evaluate()