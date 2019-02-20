#-----------------------------------------------------------------------
# Program name: Assignment3.py
# Author: Daniel Benitez
# Date: 02/26/2019
# Purpose: Allow users to determine their voter polling station 
#-----------------------------------------------------------------------
# GLOBAL VARIABLE DEFINITIONS (Use only until functions)
age = 1
zipcode = 0
# Variable Type: Variable list separated by commas
# int
#-----------------------------------------------------------------------
# CONSTANT DEFINITIONS

#-----------------------------------------------------------------------
# CLASS DEFINITIONS

#-----------------------------------------------------------------------
# FUNCTION DEFINITIONS

#-----------------------------------------------------------------------
# PROGRAM'S MAIN LOGIC
#
print("VOTER ELIGIBILITY AND POLLING STATION PROGRAM\n\n")

while age != 0:
    # Prompt user for Age.
    age = int(input("Enter your age: "))

    if age == 0:
        # Program ends if user entered 0.
        print("Program has ended.")
    elif age < 18:
        # Tell user they are unable to vote if age is < 18.
        print("YOU ARE INELIGIBLE TO VOTE.\n")
    elif age >= 18:
        # Prompt user for zipcode.
        zipcode = int(input("Enter your zip code: "))
        
        # If zipcode is valid then display address related, otherwise send error.
        if zipcode == 93305:
            print("Your polling station is 123 Panorama Drive.\n\n")
        elif zipcode == 93306:
            print("Your polling station is 6143 Fairfax Drive.\n\n")
        elif zipcode == 93307:
            print("Your polling station is 21121 B Street\n\n")
        elif zipcode == 93308:
            print("Your polling station is 863 Desmond Ct.\n\n")
        elif zipcode == 93309:
            print("Your polling station is 7332 Del Canto Ct.\n\n")
        else:
                print("Error –unknown zip code\n")



input("\nRun complete. Press the Enter key to exit.")

