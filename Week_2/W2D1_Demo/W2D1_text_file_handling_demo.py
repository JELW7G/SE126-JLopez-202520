#W2D1 - Text File Handling Intro Demo

#STEP 1: import the csv library
import csv

total_records = 0 #holds total number of records in file

#STEP 2: connect to file
#--connected to file---------------------------------
#include relative file path in open() - make sure \ switches to /
with open("Week_2/W2D1_Demo/simple.csv") as csvfile:
    #make sure to indent inside of code block

    #allow the csv.reader() to access and red the file path; stores contents to 'file' [a 2D list / matrix / table]
    file = csv.reader(csvfile)

    #print for headers
    print(f"{'NAME':10} {'NUM':3} {'COLOR'}\n")

    #STEP 3: process through every recored (row) in the file
    for record in file:
        #add +1 total_records to keep accurate count of recs
        total_records += 1

        #print(record) #entire record/row data as a list

        name = record[0]        #name field
        number = record[1]      #number field
        color = record[2]       #color field

        print(f"{name:10} {number:3} {color.title()}")
#--disconnected from file----------------------------
print(f"\nTOTAL RECORDS: {total_records}\n")