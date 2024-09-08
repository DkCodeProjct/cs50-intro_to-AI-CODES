# i Enjoyed During this project..

   * didnt learn much but i did this cos. i havent code for like 5 days
 so this is a warmup project

   * however i learned how to rm a column from a csv
 
   * also i learned about what is [ next ] use  for in csv

-------------

    // Count how many fieldnames
    with open('lung1.csv') as file:
        reader = csv.reader(file)
        fieldnm = next(reader)  ## This reads and stores the Header row
    numFieldnm = len(fieldnm)

    print(f"The CSV file has {numFieldnm} fieldnames (columns).")



    //Load data from the CSV file
    with open('lung1.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  ## This  Skip the Header

-------------

