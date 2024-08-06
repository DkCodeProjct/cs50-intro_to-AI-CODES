import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    intEvidenceData = []
    intLabelData = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            
            # float data  --->
            adminDuration = float(row['Administrative_Duration'])
            infoDuration = float(row['Informational_Duration'])
            productDuration = float(row['ProductRelated_Duration'])
            bounceRate = float(row['BounceRates'])
            exitRate = float(row['ExitRates'])
            pageVal = float(row['PageValues'])
            specialDay = float(row['SpecialDay'])


            # int Data  --->
            admin = int(row['Administrative'])
            info = int(row['Informational'])
            productRel = int(row['ProductRelated'])


            if row['Month'] == 'Jan':
                month = 0
            
            elif row['Month'] == 'Feb':
                month = 1
            
            elif row['Month'] == 'Mar':
                month = 2
            
            elif row['Month'] == 'Apr':
                month = 3
            
            elif row['Month'] == 'May':
                month = 4
            
            elif row['Month'] == 'Jun':
                month = 5
            
            elif row['Month'] == 'Jul':
                month = 6
            
            elif row['Month'] == 'Aug':
                month = 7
            
            elif row['Month'] == 'Sep':
                month = 8
            
            elif row['Month'] == 'Oct':
                month = 9
            
            elif row['Month'] == 'Nov':
                month = 10
            
            elif row['Month'] == 'Dec':
                month = 11
            
            os = int(row['OperatingSystems'])
            brwsor = int(row['Browser'])
            region = int(row['Region'])
            traficType = int(row['TrafficType'])
            
            if row['VisitorType'] == 'Returning_Visitor':
                visitor = 1
            
            elif row['VisitorType'] == 'New_Visitor':
                visitor = 0
            
            
            # init var[weekend] with default val cos unboubndLocalEror
            weekend = None
            if row['Weekend'] == 'True':
                weekend = 1
            
            elif row['Weekend'] == 'False':
                weekend = 0

            # list of evidence
            evidence = [
                #float Data
                adminDuration,
                infoDuration,
                productDuration,
                bounceRate,
                exitRate,
                pageVal,
                specialDay,

                #int Data
                admin,
                info,
                productRel,
                month,
                os,
                traficType,
                brwsor,
                region,
                visitor,
                weekend,

            ]
            intEvidenceData.append(evidence)
           
            # init var[label] with defaualt val cos unboubndLocalEror
            label = None
            if row['Revenue'] == 'True':
                label = 1
            elif row['Revenue'] == 'False':
                label = 0
            
            intLabelData.append(label)
        
        return intEvidenceData, intLabelData


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)
    
    return model

def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    
    truePositiv = 0
    trueNegativ = 0
    falsePositiv = 0
    falseNegativ = 0

    for trueLable, predictlable in zip(labels, predictions):
        if trueLable == 1 and predictlable == 1:
            truePositiv += 1
        elif trueLable == 1 and predictlable == 0:
            falseNegativ += 1
        elif trueLable == 0 and predictlable == 1:
            falsePositiv += 1
        elif trueLable == 0 and predictlable == 0:
            trueNegativ += 1
    
    sensivity = truePositiv / (truePositiv + falseNegativ)
    specifity = trueNegativ / (trueNegativ + falsePositiv)

    return sensivity, specifity


if __name__ == "__main__":
    main()
