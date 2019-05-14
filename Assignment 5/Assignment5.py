#-----------------------------------------------------------------------
# Program name: Assignment5.py
# Author: Daniel Benitez
# Date: 4/2/2019
# Purpose: Search city and state based on a zipcode the user entered
#          from a text file listing all zipcodes, cities and states.
#-----------------------------------------------------------------------
# GLOBAL VARIABLE DEFINITIONS (Use only until functions)

# Variable Type: Variable list separated by commas

#-----------------------------------------------------------------------
# CONSTANT DEFINITIONS

#-----------------------------------------------------------------------
# CLASS DEFINITIONS

#-----------------------------------------------------------------------
# FUNCTION DEFINITIONS


def checkFile():

    try:
        # Going to check if the file exists and set to read mode.
        zipcodeFile = open("zipcodes.txt", "r")
        newList = list(zipcodeFile)
        prompt(True, newList)
    except IOError:
        # If file does not exist, send error and end program.
        print("Error - zipcodes.txt does not exist\n")
        prompt(False, '')

def searchZip(n, l):

    zipList = l;
    # Going through the list and splitting the zipcode from the rest
    # using the split method.
    for i in zipList:
        zipFinder = i.split(',')[0]  # i.e first item before comma.

        if n == zipFinder:

            # If zipcode does exist, split the city and state also.
            city = i.split(',')[1]   # i.e the second iten after comma.
            state = i.split(',')[2]  # i.e the third item after comma.

            # Return the city and state found.
            return print("\n\tThe city is " + city + " and the state is " + state)

    # If zipcode not found, return message.
    return print("Zipcode does not exist.\n")

def prompt(b, l):
    print ("\nZipcode Lookup Program\n")
    # If file does not exist, the loop is skipped.
    # Set loop to true until 'Enter' is pressed.
    while b == True:
        zipcode = input("Enter a zip code to find (Press Enter key alone to stop): ")

        if zipcode == '':
            return input("\nRun complete. Press the Enter key to exit.")
        else:
         searchZip(zipcode, l)

    


    
#-----------------------------------------------------------------------
# PROGRAM'S MAIN LOGIC
#

checkFile()
input("\nRun complete. Press the Enter key to exit.")
