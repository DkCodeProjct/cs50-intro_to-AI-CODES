import csv

inputFile = 'lung0.csv'
columnToRm = 'LUNG_CANCER'
outputFile = 'lung1.csv'

            
with open(inputFile, 'r') as file:
    reader = csv.DictReader(file)
    fieldnm = [field for field in reader.fieldnames if field != columnToRm]

    with open(outputFile, 'w', newline='') as out:
        writr =  csv.DictWriter(out, fieldnames=fieldnm)
        writr.writeheader()
        for row in reader:
            del row[columnToRm]
            writr.writerow(row)

print(f'{columnToRm} colmn has rm')