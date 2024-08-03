import csv

inputfile = 'smmh0.csv'
outputfile = 'smmh1.csv'

with open(inputfile, 'r') as infile, open(outputfile, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldname = reader.fieldnames + ['class']
    writer = csv.DictWriter(outfile, fieldnames=fieldname)
    writer.writeheader()

    for row in reader:
        if (row['6. Do you use social media?'].lower() == 'yes' and 
            int(row['9. How often do you find yourself using Social media without a specific purpose?']) > 1 and
            int(row['10. How often do you get distracted by Social media when you are busy doing something?']) > 1 and
            int(row["12. On a scale of 1 to 5, how easily distracted are you?"]) > 1 and
            int(row["13. On a scale of 1 to 5, how much are you bothered by worries?"]) > 1 and
            int(row["14. Do you find it difficult to concentrate on things?"]) > 1 and
            int(row["15. On a scale of 1-5, how often do you compare yourself to other successful people through the use of social media?"]) > 1 and
            int(row["16. Following the previous question, how do you feel about these comparisons, generally speaking?"]) > 1 and
            int(row["17. How often do you look to seek validation from features of social media?"]) > 1 and
            int(row["18. How often do you feel depressed or down?"]) > 1 and
            int(row["19. On a scale of 1 to 5, how frequently does your interest in daily activities fluctuate?"]) > 1 and
            int(row["20. On a scale of 1 to 5, how often do you face issues regarding sleep?"]) > 1):
                classData = 1
        else:
            classData = 0
        
        row['class'] = classData
        writer.writerow(row)
