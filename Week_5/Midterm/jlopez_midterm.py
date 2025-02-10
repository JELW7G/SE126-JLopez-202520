#Joseph Lopez
#SE126.04
#Midterm - Prompt #1 "westeros.csv"
#2/10/2025

#PROGRAM PROMPT: Using the file named above, read the data from the file and store to 1D parallel lists. Once the lists have been fully populated with file data, create a new list to hold an office number for each of the employees. Office numbers should start at 100 and not exceed 200. Assign each employee an office number and store to the newly created list, then process through the six lists to display all of the data to the user as well as the total number of records in the file. Once all of the data has been displayed, write all of the list data to a new file called ‘midterm_choice1.csv’, where each employee’s information is found on one record in the file and their data is separated by a comma (additional empty line in resulting file is okay). Finally, create a sequential search program that allows a user to repeatedly search the employee information stored in the lists based on the following menu:
#Westeros Services Directory Search
#   1. Search by EMAIL
#   2. Search by DEPARTMENT
#   3. EXIT
#For option 1: When a searched-for item is found, print all data* in the program on the specific employee from the lists. If they are not found, alert the user.
#For option 2: When a searched for item is found, print all data* in the program on all employees that match the criteria. If no one matches the searched-for criteria, alert the user. The user should not be able to quit the search program unless they choose option 3, to exit.


#MAIN CODE:
import csv

#initiailizing lists
first_name = []
last_name = []
email = []
department = []
extension = []
total_records = 0

#------connect with westeros.csv------
with open("Week_5/Midterm/westeros.csv") as csvfile:
    file = csv.reader(csvfile)

    for record in file:
        first_name.append(record[0])
        last_name.append(record[1])
        email.append(record[2])
        department.append(record[3])
        extension.append(record[4])
#------disconnect from westeros.csv------

#creating and appending the office_num list
office_num = []
num = 100

for i in range(0, len(first_name)):
    office_num.append(num)
    num += 1

#creating and adding data to midterm_choice1.csv, including adding office numbers
file = open("Week_5/Midterm/midterm_choice1.csv", "w")
for i in range(len(first_name)):
    file.write(f"{first_name[i]},{last_name[i]},{email[i]},{department[i]},{extension[i]},{office_num[i]}\n")
    total_records += 1

file.close()

#headers for list
print(f"{'FNAME':10} {'LNAME':10} {'EMAIL':30} {'DEPARTMENT':25} {'EXT.':4} {'OFFICE':4}\n")

#displaying all user data
for i in range(0, len(first_name)):
    print(f"{first_name[i]:10} {last_name[i]:10} {email[i]:30} {department[i]:25} {extension[i]:4} {office_num[i]:4}\n")

print(total_records)
#sequential search start
print("\n\nWelcome to the Westeros Employee Search Program\n\n")

answer = input("Would you like to begin searching? [y/n]: ").lower()

#error checking
while answer != "y" and answer != "n":
    print("*INVALID ENTRY*")
    answer = input("Would you like to begin searching? [y/n]: ").lower()

#main loop
while answer == "y":
    #prompting user for option selection
    print("\tSEARCH MENU OPTIONS\n")
    print("1. Search by EMAIL")
    print("2. Search by DEPARTMENT")
    print("3. EXIT\n")
    option = input("Enter your search type [1-3]: ")

    #option 1: search by email
    if option == "1":
        print("\tSearch by EMAIL\n")

        #"x" is our invalid index string
        found = "x"

        search_email = input("Enter the EMAIL of the employee you are searching for: ")

        #performs search
        for i in range(0, len(email)):
            if search_email.lower() == email[i].lower():
                found = i
        
        #displays search results
        if found != "x":
            print(f"\nThe search for {search_email} was SUCCESSFUL!\n")
            print(f"{first_name[found]:10} {last_name[found]:10} {email[found]:30} {department[found]:25} {extension[found]:4} {office_num[found]:4}")
        else:
            print(f"\nThe search for {search_email} was *NOT* SUCCESSFUL!")
            print(f"Please check your spelling and try again.\n")

    #option 2: search by department
    elif option == "2":
        print("\tSearch by DEPARTMENT\n")

        #'found' will be a list to store multiple searches
        found = []

        search_department = input("Enter the DEPARTMENT of the employee(s) you are searching for: ")

        #performs search
        for i in range(0, len(department)):
            if search_department.lower() == department[i].lower():
                found.append(i)

        #displays search result
        if not found:
            print(f"\nThe search for {search_department} was *NOT* SUCCESSFUL!")
            print(f"Please check your spelling and try again.\n")
        
        else:
            print(f"\nThe search for {search_department} was SUCCESSFUL!\n")

            for i in range(0, len(found)):
                print(f"{first_name[found[i]]:10} {last_name[found[i]]:10} {email[found[i]]:30} {department[found[i]]:25} {extension[found[i]]:4} {office_num[found[i]]:4}")

    #option 3: exit
    elif option == "3":
        print("\tEXITING PROGRAM")
        answer = "n"
    
    #error checking
    else:
        print("*INVALID ENTRY*")

    if option == "1" or option == "2":
        answer = input("Would you like to do another search? [y/n]: ").lower()
        #error checking
        while answer != "y" and answer != "n":
            print("*INVALID ENTRY*")
            answer = input("Would you like to do another search? [y/n]: ").lower()