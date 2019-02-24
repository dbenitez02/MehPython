# Better version of Assignment 1.
# Utilize functions and avoid global variables.

def sales(n):
    TAX = float(0.08)

    sub = float(n) # I guess I have to manually convert the parameter into a float.
    salesTax = sub * TAX
    totalSales = salesTax + sub

    print("Sales amount is ${:,.2f}".format(sub))
    print("Sales tax is ${:,.2f}".format(salesTax))
    print("Total sales is ${:,.2f}".format(totalSales))

# ---Main code---
sales(input("Enter sales amount: "))