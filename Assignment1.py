#-----------------------------------------------------------------------
# Program name: Assignment 1 
# Author: Daniel Benitez
# Date: 01/22/2019
# Purpose: Output the total sale.
#-----------------------------------------------------------------------
# GLOBAL VARIABLE DEFINITIONS (Use only until functions)
#
sales = 0
salesTax = 0
totalSales = 0
#-----------------------------------------------------------------------
# CONSTANT DEFINITIONS
TAX = float(0.08)

#-----------------------------------------------------------------------
# CLASS DEFINITIONS

#-----------------------------------------------------------------------
# FUNCTION DEFINITIONS

#-----------------------------------------------------------------------
# PROGRAM'S MAIN LOGIC
#
sales = float(input("Enter the sales amount: "))              # Prompt user to enter a number. Store value as float.
salesTax = (sales * TAX)                                      # Multiply sales and tax to get sales tax.
totalSales= ((sales * TAX) + sales)                           # Calculate total sales.

# Print sales, sales tax, and total amount in the appropiate format. Ex: $1,000.00
print("\n\nThe sales amount is ${:,.2f}".format(sales))
print("The sales tax is ${:,.2f}".format(salesTax))  
print("The total sale is ${:,.2f}".format(totalSales))  

input("\n\nRun complete. Press the Enter key to exit.")  # Hit that 'enter' button to stop the program.
