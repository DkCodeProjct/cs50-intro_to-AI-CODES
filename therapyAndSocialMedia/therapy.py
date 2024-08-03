# 
# CSV TO USE:: 
#       [[ smmh1.csv ]]
# #


import csv
import random
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

csvDataFile = 'smmh1.csv'
data = pd.DataFrame(csvDataFile)

data['2. Gender'] = data['2. Gender'].map({'Male':0, 'Femal':1})

data['3. Relationship Status'] = data['3. Relationship Status'].map({'Single':0 ,'In a relationship':1})

data['6. Do you use social media?'] = data['6. Do you use social media?'].map({'No':0 ,'Yes':1})

ocupationMaping = {
    'Student': 0,
    'Employed': 1,
    'Unemployed': 2,
    'Retired': 3,
    'Other': 4
}
data['4. Occupation Status'] = data['4. Occupation Status'].map(ocupationMaping)

socailMedeaPlatforms = {
    'Facebook': 0,
    'Twitter': 1,
    'Instagram': 2,
    'YouTube': 3,
    'Discord': 4,
    'Reddit': 5
}

# gpt genarated
data['7. What social media platforms do you commonly use?'] = data['7. What social media platforms do you commonly use?'].apply(
    lambda x: [socailMedeaPlatforms[platform] for platform in x.split(', ') if platform in socailMedeaPlatforms]
)

data.drop(columns=['7. What social media platforms do you commonly use?'], inplace=True)

data = pd.read_csv(csvDataFile)

features = [
    'Average time spent on social media every day',
    'Frequency of using social media without a specific purpose',
    'Frequency of getting distracted by social media when busy',
    'Feelings of restlessness if social media is not used',
    'Ease of distraction (scale of 1 to 5)',
    'Level of worry (scale of 1 to 5)',
    'Difficulty concentrating',
    'Frequency of comparing oneself to successful people on social media (scale of 1 to 5)',
    'Feelings about these comparisons',
    'Frequency of seeking validation from social media',
    'Frequency of feeling depressed or down',
    'Fluctuation in interest in daily activities (scale of 1 to 5)',
    'Issues with sleep (scale of 1 to 5)'
]
targetVar = 'class'

x = data[features]
y = data[targetVar]

xTrain, yTrain, xTest, yTest = train_test_split(x, y, test_size=0.3, random_state=42)

scalr = StandardScaler()
xTrain = scalr.fit_transform(xTrain)
xTest = scalr.fit_transform(xTest)

model = RandomForestClassifier()
model.fit(xTrain, yTrain)

targerPredict = model.predict(xTest)

accuracy = accuracy_score(yTest, targerPredict)
print(f'Accuracy, :{accuracy}')

print(classification_report(yTest, targerPredict))

# Analyze feature importance
importances = model.feature_importances_
feature_importance_df = pd.DataFrame({
    'Feature': features,
    'Importance': importances
})