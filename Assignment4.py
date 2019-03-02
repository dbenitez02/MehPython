#-----------------------------------------------------------------------
# Program name: Assignment4.py
# Author: Daniel Benitez
# Date: 03/05/2019
# Purpose: Output conversions for Farhenheit to Celsuis, Miles to Kilometers,
# and Pounds to Kilograms. 
#-----------------------------------------------------------------------
# GLOBAL VARIABLE DEFINITIONS (Use only until functions)
# Variable Type: Variable list separated by commas

#-----------------------------------------------------------------------
# CONSTANT DEFINITIONS

#-----------------------------------------------------------------------
# CLASS DEFINITIONS

#-----------------------------------------------------------------------
# FUNCTION DEFINITIONS

# Calculate conversion to Celsius and output result.
def tempConversion():
    farh = float(input("\nPlease enter a temperature to convert to Celsuis: "))
    celsuis = ((farh + 32.00) / 1.8)
    return print("{:.3f}f is {:.3f}c\n".format(farh, celsuis))

# Calculate conversion to Kilometers and output result.
def distConversion():
    mile = float(input("\nEnter number of miles to convert to kilometers: "))
    kilometer = (mile / (0.621371192237))
    return print("{:.3f} miles is {:.3f} kilometers.\n".format(mile, kilometer))

# Calculate conversion to Kilograms and ouput result.
def weightConversion():
    pound = float(input("\nEnter number of pounds to convert to kilograms: "))
    kilogram = (pound / 2.2)
    return print("{:.3f} pounds is {:.3f} kilograms\n".format(pound, kilogram))

# The main menu.
def menu():

    while True:
        print("CONVERSION PROGRAM\n\n")

        print("T = Convert Farhenheit to Celsius")
        print("D = Convert Miles to Kilometers")
        print("W = Convert Pounds to Kilograms\n\n")

        k = str(input("Select conversion to perform 'T'emperature, 'D'istance, 'W'eight  or 'Q'uit? ").upper())

        # Check for correct input otherwise send error message.
        # If valid, call function 
        if k == 'T':
            tempConversion()
        elif k == 'D':
            distConversion()
        elif k == 'W':
            weightConversion()
        elif k == 'Q':
            return input("\nRun complete. Press the Enter key to exit.")
        else:
            print("Error -Invalid option selected.  You may only enter T, D or W.\n")

#-----------------------------------------------------------------------
# PROGRAM'S MAIN LOGIC
#

# Thats all..
menu()


