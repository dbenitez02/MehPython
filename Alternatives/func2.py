# A better variation of assignment 2 same format as Assignment 1.

def tempConversion():
    farh = float(input("\n\nPlease a temperature to convert to Celsuis: "))
    celsuis = ((farh - 32.00) / 1.8)
    return print("{:.3f}f is {:.3f}c".format(farh, celsuis))

def distConversion():
    mile = float(input("Enter number of miles to convert to kilometers: "))
    kilometer = (mile / (0.621371192237))
    return print("{:.3f} miles is {:.3f} kilometers.".format(mile, kilometer))

def weightConversion():
    pound = float(input("Enter number of pounds to convert to kilograms: "))
    kilogram = (pound / 2.205)
    return print("{:.3f} pounds is {:.3f} kilograms".format(pound, kilogram))

def menu(k):
    if k == 'T':
        tempConversion()
    elif k == 'D':
        distConversion()
    elif k == 'W':
        weightConversion()
    else:
        return print("Invalid input boi.")

# ---Main code---

print("Welcome to conversion of shenanigans!!\n\n")
menu(str(input("Press w for weight, d for distance, or t for temp: ")).upper())


# Lol all in two lines. Well really one line, but its fun to let users know whats going on.


