import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.impute import SimpleImputer

class NeedForTherapy:
    def __init__(self, csvFile):
        self.csvFile = csvFile
        self.data = None
        self.model = None
        self.scalar = None
        self.imputer = None
        self.featurs = [
            '8. What is the average time you spend on social media every day?',
            '9. How often do you find yourself using Social media without a specific purpose?',
            '10. How often do you get distracted by Social media when you are busy doing something?',
            '11. Do you feel restless if you haven\'t used Social media in a while?',
            '12. On a scale of 1 to 5, how easily distracted are you?',
            '13. On a scale of 1 to 5, how much are you bothered by worries?',
            '14. Do you find it difficult to concentrate on things?',
            '15. On a scale of 1-5, how often do you compare yourself to other successful people through the use of social media?',
            '16. Following the previous question, how do you feel about these comparisons, generally speaking?',
            '17. How often do you look to seek validation from features of social media?',
            '18. How often do you feel depressed or down?',
            '19. On a scale of 1 to 5, how frequently does your interest in daily activities fluctuate?',
            '20. On a scale of 1 to 5, how often do you face issues regarding sleep?'
        ]

        self.targertVar = 'class'

    def loadData(self):
        self.data = pd.read_csv(self.csvFile)
    
    def preprocesData(self):
        self.data['2. Gender'] = self.data['2. Gender'].map({'Male': 0, 'Female': 1})
        self.data['3. Relationship Status'] = self.data['3. Relationship Status'].map({'Single': 0, 'In a relationship': 1})
        self.data['6. Do you use social media?'] = self.data['6. Do you use social media?'].map({'No': 0, 'Yes': 1})

        occupation_mapping = {
            'Student': 0,
            'Employed': 1,
            'Unemployed': 2,
            'Retired': 3,
            'Other': 4
        }
        self.data['4. Occupation Status'] = self.data['4. Occupation Status'].map(occupation_mapping)

        time_spent_mapping = {
            'Less than 1 hour': 0,
            'Between 1 and 3 hours': 1,
            'Between 2 and 3 hours': 1,
            'More than 3 hours': 2,
            'More than 5 hours': 3
        }
        self.data['8. What is the average time you spend on social media every day?'] = self.data['8. What is the average time you spend on social media every day?'].map(time_spent_mapping)

        social_media_platforms = {
            'Facebook': 0,
            'Twitter': 1,
            'Instagram': 2,
            'YouTube': 3,
            'Discord': 4,
            'Reddit': 5
        }
        self.data['7. What social media platforms do you commonly use?'] = self.data['7. What social media platforms do you commonly use?'].apply(
            lambda x: [social_media_platforms[platform] for platform in x.split(', ') if platform in social_media_platforms]
        )
    
    def handleMissingVal(self):
        self.imputer = SimpleImputer(strategy='mean')
        self.data[self.featurs] = self.imputer.fit_transform(self.data[self.featurs])

    def splitData(self):
        x = self.data[self.featurs]
        y = self.data[self.targertVar]
        return train_test_split(x, y, test_size=0.3, random_state=42)

    def scaleData(self, xTrain, xTest):
        self.scalar = StandardScaler()
        xTrainScale = self.scalar.fit_transform(xTrain)
        xTestScale = self.scalar.transform(xTest)
        return xTrainScale, xTestScale
    
    def trainingModel(self, xtrain, ytrain):
        self.model = RandomForestClassifier()
        self.model.fit(xtrain, ytrain)
    
    def evaluate(self, xTest,   yTest):
        yPred = self.model.predict(xTest)
        accuracy = accuracy_score(yTest, yPred)
        print(f'Accuracy: {accuracy}')
        print(classification_report(yTest, yPred))
        return yPred
    
    def featurImportance(self):
        importances = self.model.feature_importances_
        feature_importance_df = pd.DataFrame({
            'Feature': self.featurs,
            'Importance': importances
        })
        print(feature_importance_df) 


csvFile = 'smmh1.csv'
model = NeedForTherapy(csvFile)
model.loadData()
model.preprocesData()
model.handleMissingVal()
x_train, x_test, y_train, y_test = model.splitData()
x_train_scaled, x_test_scaled = model.scaleData(x_train, x_test)
model.trainingModel(x_train_scaled, y_train)
model.evaluate(x_test_scaled, y_test)
model.featurImportance()