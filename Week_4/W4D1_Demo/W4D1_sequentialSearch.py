#W4D1 - Sequential Search

#PROGRAM PROMPT: We will continue to work with the class_grades.csv file, as used in the W3D2 demo. We will practice connecting to a file, storing the file data into parallel lists, and creating new data for each student record based on these lists. We will then build a sequential search program which will allow us to find students in the file, and write data regarding them to a newly created file in our repository.

#this file uses: class_grades.csv

#--IMPORTS-----------------------------------------------
import csv
#--FUNCTIONS---------------------------------------------
def letter(num):
    if num >= 90:
        let = "A"
    elif num >= 80:
        let = "B"
    elif num >= 70:
        let = "C"
    elif num >= 60:
        let = "D"
    elif num < 60:
        let = "F"
    else:
        let = "ERROR"

    return let #'let' value replaces the function call in the main executing code

#--MAIN EXECUTING CODE-----------------------------------

#create empty lists to hold the file data 
fName = []
lName = []
test1 = []
test2 = []
test3 = []

with open("Week_3/W3D2_Demo/class_grades.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #append the file data into appropriate lists
        fName.append(rec[0])
        lName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#disconected from file -- can still access the stored data via the lists 

#process the list data to calc an avg score for each student, and find a letter grade equivalent

num_avg = [] #will hold each student's numeric average of test scores
let_avg = [] #will hold each student's letter average of test scores

for i in range(0, len(fName)):

    #calculate average of current student
    a = (test1[i] + test2[i] + test3[i]) / 3
    #add average to num_avg list
    num_avg.append(a)  #can also do: num_avg.append((test1[i] + test2[i] + test3[i]) / 3)

    l = letter(a) #return value of letter() stored to l
    let_avg.append(l)   #can also do: let_avg.append(letter(a))

#process the lists to display all student data back to the user
print(f"{'FNAME':10}  {'LNAME':10}  {'T1':3}  {'T2':3}  {'T3':3}  {'# AVG':6}  {'L AVG'}")
print("---------------------------------------------------------------------------------")
for i in range(0, len(fName)):
    print(f"{fName[i]:10}  {lName[i]:10}  {test1[i]:3}  {test2[i]:3}  {test3[i]:3}  {num_avg[i]:6.2f}  {let_avg[i]}")

print("---------------------------------------------------------------------------------")

print(f"There are {len(fName)} students in the file. ")



#write a program that allows a user to repeatedly search for a student by their last name or their letter grade; when a specific user is found, display all data relevant on that user, when not found alert the user. When searching by letter grade, display all of the students' data when found, or alert the user that no student grades fit that description

print("\n\nWelcome to the Student Search Program\n\n")

answer = input("Would you like to begin searching? [y/n]: ").lower()

while answer == "y":
    #get search type from user
    print("\tSEARCH MENU OPTIONS")
    print("1. Search by LAST name")
    print("2. Search by LETTER GRADE")
    print("3. EXIT")
    search_type = input("Enter your search type [1-3]: ")

    if search_type == "1":
        print("\tSEARCH BY LAST NAME")

        found = -1 #invalid index number, will use to check later to see if a student has been found

        #get search item from user 
        search_name = input("Enter the LAST NAME of the student you are searching for: ")

        #perform search 
        for i in range(0 , len(lName)):
            #the FOR LOOP allows for the "sequence" part -> from beginning to end
            if search_name.lower() == lName[i].lower():
                #the IF STATEMENT allows for the "search" part
                found = i #make found the current index, can be used later to display

        #display results
        if found != -1: 
            #last name has been found! display data:
            print(f"Your search for {search_name} was FOUND!")
            print(f"{fName[found]:10}  {lName[found]:10}  {test1[found]:3}  {test2[found]:3}  {test3[found]:3}  {num_avg[found]:6.2f}  {let_avg[found]}")
        else:
            print(f"Your search for {search_name} was *NOT* FOUND!")
            print(f"This is a cAsE sEnSiTiVe program - check your spelling and casing and try again.")


    elif search_type == "2":
        print("\tSEARCH BY LETTER GRADE")
        found = [] #creates empty list to gather and store found index values

        #get search item from user 
        search_grade = input("Enter the LETTER GRADE of the students you are searching for: ")

        #perform search 
        for i in range(0 , len(let_avg)):
            #the FOR LOOP allows for the "sequence" part -> from beginning to end
            if search_grade.upper() == let_avg[i]:
                #the IF STATEMENT allows for the "search" part
                found.append(i) #add the current index (found), can be used later to display

        #display results
        if not found: #the list is empty  
            print(f"Your search for {search_grade} was *NOT* FOUND!")
            print(f"This is a cAsE sEnSiTiVe program - check your spelling and casing and try again.")
            
        else:
            print(f"Your search for {search_grade} was FOUND!")

            #found is a list with multiple pieces of data - must use a FOR LOOP to see all
            for i in range(0, len(found)):
                print(f"{fName[found[i]]:10}  {lName[found[i]]:10}  {test1[found[i]]:3}  {test2[found[i]]:3}  {test3[found[i]]:3}  {num_avg[found[i]]:6.2f}  {let_avg[found[i]]}")
            
    elif search_type == "3":
        print("\tEXITING")
        answer = "n"
    else:
        print("*INVALID ENTRY*")
    #build a way out of the loop 
    if search_type == "1" or search_type == "2": #only when user doesnt specify 3 to exit
        answer = input("Would you like to search again? [y/n]: ").lower()
