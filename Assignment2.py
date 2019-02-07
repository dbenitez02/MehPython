#-----------------------------------------------------------------------
# Program name: Assignment 2
# Author: Daniel Benitez
# Date: 01/22/2019
# Purpose: Output conversions for Farhenheit to Celsuis, Miles to Kilometers,
# and Pounds to Kilograms. 
#-----------------------------------------------------------------------
# GLOBAL VARIABLE DEFINITIONS (Use only until functions)
#
farhenheit = 0
miles = 0
pound = 0
celsuis = 0
kilometer = 0
kilogram = 0
key = ''
#-----------------------------------------------------------------------
# CONSTANT DEFINITIONS
FARH_OFFSET = float(32)
TEMP_CONVERSION = float(1.8)
DIST_CONVERSION = float(0.621371192237)
WEIGHT_CONVERSION = float(2.2)
#-----------------------------------------------------------------------
# CLASS DEFINITIONS

#-----------------------------------------------------------------------
# FUNCTION DEFINITIONS

#-----------------------------------------------------------------------
# PROGRAM'S MAIN LOGIC
#

print("CONVERSION PROGRAM\n\n")

# Print options
print("T = Convert Farhenheit to Celsius")
print("D = Convert Miles to Kilometers")
print("W = Convert Pounds to Kilograms\n\n")

key = str(input("Selectconversion to perform ('T'emperature, 'D'istance, 'W'eight)? ")).capitalize()

# If T, convert from farhenheit to Celcius.
if key == 'T':
    farhenheit = float(input("Enter a number in Farhenheit: "))
    celsuis = (farhenheit - FARH_OFFSET) / TEMP_CONVERSION
    print("{:.3f} F is {:.3f} C.\n\n".format(farhenheit, celsuis))
    
# If D, convert from miles to kilometers.
elif key == 'D':
    miles = float(input("Enter a number in miles: "))
    kilometer = miles / DIST_CONVERSION
    print("{:.3f} miles is {:.3f} kilometers.\n\n".format(miles, kilometer))
    
# If W, convert from pounds to kilograms
elif key == 'W':
    pound = float(input("Enter a number in pounds: "))
    kilogram = pound / WEIGHT_CONVERSION
    print("{:.3f} pounds is {:.3f} kilograms.\n\n".format(pound, kilogram))

# Print an error statement if input is invalid.
else:
    print("Invalid option selected. You may only enter, T, D, or W.\n\n")

input("Run complete. Press the Enter key to exit.")

