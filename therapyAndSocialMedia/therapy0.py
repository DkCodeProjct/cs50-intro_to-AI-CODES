import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.impute import SimpleImputer

# Read the CSV file
csvDataFile = 'smmh1.csv'
data = pd.read_csv(csvDataFile)

data['2. Gender'] = data['2. Gender'].map({'Male': 0, 'Female': 1})
data['3. Relationship Status'] = data['3. Relationship Status'].map({'Single': 0, 'In a relationship': 1})
data['6. Do you use social media?'] = data['6. Do you use social media?'].map({'No': 0, 'Yes': 1})

occupation_mapping = {
    'Student': 0,
    'Employed': 1,
    'Unemployed': 2,
    'Retired': 3,
    'Other': 4
}
data['4. Occupation Status'] = data['4. Occupation Status'].map(occupation_mapping)

time_spent_mapping = {
    'Less than 1 hour': 0,
    'Between 1 and 3 hours': 1,
    'Between 2 and 3 hours': 1,
    'More than 3 hours': 2,
    'More than 5 hours': 3
}
data['8. What is the average time you spend on social media every day?'] = data['8. What is the average time you spend on social media every day?'].map(time_spent_mapping)

social_media_platforms = {
    'Facebook': 0,
    'Twitter': 1,
    'Instagram': 2,
    'YouTube': 3,
    'Discord': 4,
    'Reddit': 5
}
# gpt genarated
data['7. What social media platforms do you commonly use?'] = data['7. What social media platforms do you commonly use?'].apply(
    lambda x: [social_media_platforms[platform] for platform in x.split(', ') if platform in social_media_platforms]
)

# Features and target variable
features = [
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

targetVar = 'class'

imputer = SimpleImputer(strategy='mean')
data[features] = imputer.fit_transform(data[features])

xTrain, xTest, yTrain, yTest = train_test_split(data[features], data[targetVar], test_size=0.3, random_state=42)

scaler = StandardScaler()
xTrain = scaler.fit_transform(xTrain)
xTest = scaler.transform(xTest)

model = RandomForestClassifier()
model.fit(xTrain, yTrain)


yPred = model.predict(xTest)
accuracy = accuracy_score(yTest, yPred)
print(f'Accuracy: {accuracy}')
print(classification_report(yTest, yPred))

importances = model.feature_importances_
feature_importance_df = pd.DataFrame({
    'Feature': features,
    'Importance': importances
})
print(feature_importance_df)
