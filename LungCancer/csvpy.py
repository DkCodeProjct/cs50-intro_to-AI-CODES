import csv
#import tensorflow as tf
#import keras
#from sklearn.model_selection import train_test_split

inputFile = 'lung,csv'
outputFile = 'lung0.csv'

with open(inputFile, 'r') as inFile, open(outputFile, 'w', newline='') as outFile:
    reader = csv.DictReader(inFile)
    fildnm = reader.fieldnames + ['class']
    writr = csv.DictWriter(outFile, fieldnames=fildnm)
    writr.writerow()

    for row in reader:
        if row['LUNG_CANCER'] == 'YES':
            classData = 1
        else:
            classData = 0
        
        row['class'] = classData
        writr.writerow(row)
        
        