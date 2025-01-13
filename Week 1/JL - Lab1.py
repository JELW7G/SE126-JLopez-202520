#Joseph Lopez
#SE126.04
#W1D2 Lab 1
#1/11/2025

#PROGRAM PROMPT: You will be writing one Python file for this project - it is a program that determines whether a meeting room is in violation of fire regulations regarding the maximum room capacity. The program will accept the maximum room capacity and the number of people attending the meeting. If the number of people is less than or equal to the maximum room capacity, the program announces that it is legal to hold the meeting and tells how many additional people may legally attend. If the number of people exceeds the maximum room capacity, the program announces that the meeting cannot be held as planned due to the fire regulation and tells how many people must be excluded in order to meet the fire regulations. The user should be allowed to enter and check as many rooms as they would like without exiting the program.

#VARIABLE DICTIONARY
#people_attending       Number of people attending the meeting
#room_capacity          Limit of people that can be in the meeting room
#over_under             Difference between 'people_attending' and 'room_capacity'
#user_response          User's response to if they would like to continue using the program
#meeting_name           User inputted name for the meeting

#-----FUNCTIONS-----
def difference(people, max_cap):
    '''This function takes the user inputted number of people attending the meeting and the user inputted maximum room capacity and finds the difference between the two.'''

    diff = people - max_cap
    return diff

def decision(response):
    '''This function asks the user wheter or not they would like to enter more meeting information or end the program.'''

    response = input("Would you like to enter another meeting's attendance information? [y/n]").lower()

    #user error checking loop
    while response != "y" and response != "n":
        print("***INVALID ENTRY!***\tPlease answer with 'y' or 'n'.")
        response = input("Would you like to enter another meeting's attendance information? [y/n]").lower()
    
    return response

#-----MAIN CODE-----

#initial variables
people_attending = 0
room_capacity = 0
over_under = 0
user_response = "y"
meeting_name = "empty"

#welcome message
print("Welcome to the Meeting Manager.")
#beginning of loop - loop is based on 'user_response' value
while user_response == "y":
    #asking user for information
    meeting_name = input("Please enter the meeting name: ")
    room_capacity = int(input(f"Please enter the maximum capacity for the room you are holding {meeting_name}: "))
    people_attending = int(input(f"Please enter the number of people that are attending {meeting_name}: "))

    #calculations
    over_under = difference(people_attending, room_capacity)

    #outputs based on 'over_under' calculations
    if over_under > 0:
        print(f"\n\t*WARNING!* You are currently over the capacity of {room_capacity} for that room, which violates fire regulations. You must remove *{over_under}* people from the meeting in order to meet fire regulations.\t")
    elif over_under < 0:
        over_under *= -1 #turns 'over_under' from a negative number into a positive number
        print(f"\n\tYou are allowed to host this meeting in accordance with fire regulations. You can have {over_under} more people in this room before you are no longer in accordance with fire regulations and cannot host the meeting.")
    else:
        #special message if 'over_under' == 0
        print(f"\n\tYou are allowed to host this meeting in accordance with fire regulations, however, you are at the maximum room capacity of {room_capacity} and cannot add any more people into this meeting.")
        
    user_response = decision(user_response)
    #end of loop

#goodbye message
print("\n\tHave a good day!")