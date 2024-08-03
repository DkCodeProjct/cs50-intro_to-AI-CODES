import csv

def reorderCsv(inputCsv, outputCsv):
    with open(inputCsv, 'r') as inputfile, open(outputCsv, 'w') as outputfile:
        reader = csv.DictReader(inputfile)
        feildnames = reader.fieldnames

        newOrder = [
            "Timestamp",
            "1. What is your age?",
            "2. Gender",
            "3. Relationship Status",
            "4. Occupation Status",
            "5. What type of organizations are you affiliated with?",
            "6. Do you use social media?",
            "7. What social media platforms do you commonly use?",
            "8. What is the average time you spend on social media every day?",
            "9. How often do you find yourself using Social media without a specific purpose?",
            "10. How often do you get distracted by Social media when you are busy doing something?",
            "11. Do you feel restless if you haven't used Social media in a while?",
            "12. On a scale of 1 to 5, how easily distracted are you?",
            "13. On a scale of 1 to 5, how much are you bothered by worries?",
            "14. Do you find it difficult to concentrate on things?",
            "15. On a scale of 1-5, how often do you compare yourself to other successful people through the use of social media?",
            "16. Following the previous question, how do you feel about these comparisons, generally speaking?",
            "17. How often do you look to seek validation from features of social media?",
            "18. How often do you feel depressed or down?",
            "19. On a scale of 1 to 5, how frequently does your interest in daily activities fluctuate?",
            "20. On a scale of 1 to 5, how often do you face issues regarding sleep?"
        ]

        writer = csv.DictWriter(outputfile, fieldnames=newOrder)
        writer.writeheader()

        for row in reader:
            newRow = {column: row[column] for column in newOrder}
            writer.writerow(newRow)

inputfile = 'smmh.csv'
outputfile = 'smmh0.csv'
reorderCsv(inputfile, outputfile)