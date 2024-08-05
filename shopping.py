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
            
            row['Administrative'] = int(row['Administrative'])
            row['Informational'] = int(row['Informational'])
            row['ProductRelated'] = int(row['ProductRelated'])

            if row['Month'] == 'Jan':
                row['Month'] = 0
            
            elif row['Month'] == 'Feb':
                row['Month'] = 1
            
            elif row['Month'] == 'Mar':
                row['Month'] = 2
            
            elif row['Month'] == 'Apr':
                row['Month'] = 3
            
            elif row['Month'] == 'May':
                row['Month'] = 4
            
            elif row['Month'] == 'Jun':
                row['Month'] = 5
            
            elif row['Month'] == 'Jul':
                row['Month'] = 6
            
            elif row['Month'] == 'Aug':
                row['Month'] = 7
            
            elif row['Month'] == 'Sep':
                row['Month'] = 8
            
            elif row['Month'] == 'Oct':
                row['Month'] = 9
            
            elif row['Month'] == 'Nov':
                row['Month'] = 10
            
            elif row['Month'] == 'Dec':
                row['Month'] = 11
            
            row['OperatingSystems'] = int(row['OperatingSystems'])
            row['Browser'] = int(row['Browser'])
            row['Region'] = int(row['Region'])
            row['TrafficType'] = int(row['TrafficType'])
            
            if row['VisitorType'] == 'Returning_Visitor':
                row['VisitorType'] = 1
            
            elif row['VisitorType'] == 'New_Visitor':
                row['VisitorType'] = 0
            
            if row['Weekend'] == 'True':
                row['Weekend'] = 1
            
            elif row['Weekend'] == 'False':
                row['Weekend'] = 0
            

            
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
    # kneighbor
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)


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
    raise NotImplementedError


if __name__ == "__main__":
    main()
