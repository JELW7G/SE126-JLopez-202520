#Joseph Lopez
#SE126.04
#W2D2 Lab 2
#2/3/2025

#PROGRAM PROMPT: You have been asked to produce a report that lists all the computers in the csv file filehandling.csv. Your report should look like the following sample output. The last line should print the number of computers in the file.

#VARIABLE DICTIONARY:
#total_computers        Displays total number of computers in the csv file
#type                   Displays what kind of machine the computer is
#brand                  Displays the brand of the computer
#cpu                    Displays what kind of CPU the computer has
#ram                    Displays how much RAM the computer has
#disk_1                 Displays the storage size of the computer's 1st disk
#num_hdd                Displays the number of hard drives the computer has
#disk_2                 Displays the storage size of the computer's 2nd disk *if it has one*
#os                     Displays what operating system the computer has
#year                   Displays what year the computer was manufactured

#-----FUNCTIONS-----


#-----MAIN CODE-----
import csv

total_computers = 0
type = ""
brand = ""
cpu = ""
ram = ""
disk_1 = ""
num_hdd = ""
disk_2 = ""
os = ""
year = ""

with open("Week_2/Lab_2/filehandling.csv") as csvfile:

    file = csv.reader(csvfile)

    #headers for list
    print(f"{'TYPE':8} {'BRAND':8} {'CPU':4} {'RAM':4} {'1ST DISK':8} {'NO. HDD':6} {'2ND DISK':8} {'OS':3} {'YR':2}\n")

    for record in file:
        #updates total_computers to match each computer in the csv file
        total_computers += 1

        #converts the type of each computer to their full description
        if record[0] == "D":
            type = "Desktop"
        else:
            type = "Laptop"
        
        #converts the brand of each computer to their full name
        if record[1] == "DL":
            brand = "Dell"
        elif record[1] == "GW":
            brand = "Gateway"
        else:
            brand = record[1]
        
        cpu = record[2]
        ram = record[3]
        disk_1 = record[4]
        num_hdd = record[5]

        #uses 'num_hdd' to determine if the computer has a 2nd disk to display
        if num_hdd == "2":
            disk_2 = record[6]
            os = record[7]
            year = record[8]
        else:
            disk_2 = " "
            os = record[6]
            year = record[7]
        
        #lists all computers and their data
        print(f"{type:8} {brand:8} {cpu:4} {ram:4} {disk_1:8} {num_hdd:6} {disk_2:8} {os:3} {year:2}")


#------disconnected from filehandling.csv------
print(f"\nTOTAL COMPUTERS: {total_computers}\n")