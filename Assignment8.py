#-----------------------------------------------------------------------
# Program name: Assignment8.py
# Author: Daniel Benitez
# Date:
# Purpose: 
#-----------------------------------------------------------------------
# GLOBAL VARIABLE DEFINITIONS (Use only until functions)

# Variable Type: Variable list separated by commas

#-----------------------------------------------------------------------
# CONSTANT DEFINITIONS

#-----------------------------------------------------------------------
# CLASS DEFINITIONS

class Employee:
    # Initiate Employee class
    # Store Name and ID of employee
    def __init__(self, employeeName, employeeNum):
        self.__employeeName = employeeName
        self.__employeeNum = employeeNum
    
    def getName(self):
        name = self.__employeeName
        return name
    
    def getNum(self):
        num = self.__employeeNum
        return num
    
    def __str__(self):
        output = "Name: " + self.__employeeName + "\n"
        output += "Employee ID: " + self.__employeeNum
        return output

class ProductionWorker(Employee):
    # Initiate ProductionWorker class under Employee class.
    # Store Shift number and Pay rate.
    def __init__(self, employeeName, employeeNum, shiftNum, hourlyPay):
        super().__init__(employeeName, employeeNum)

        self.__shiftNum = shiftNum
        self.__hourlyPay = float(hourlyPay)
    
    def getShiftNum(self):
        shift = self.__shiftNum
        return shift

    def getHourlyPay(self):
        pay = self.__hourlyPay
        return pay

    def __str__(self):
        output = "\nShift: " + self.__shiftNum + "\n"
        output += "Hourly Pay Rate: ${:.2f}".format(self.__hourlyPay) 
        return output
#-----------------------------------------------------------------------
# FUNCTION DEFINITIONS

def main():
    name = input("Enter the Name: ")
    employeeID = input("Enter the ID number: ")
    shiftNum = input("Enter Shift Number: ")
    hourlyPay = input("Enter Pay Rate: ")

    x = Employee(name, employeeID)
    y = ProductionWorker(name, employeeID, shiftNum, hourlyPay)
    
    output(x, y)

def output(a, b):
    # a is Employee() Class.
    # b is ProdectionWorker() Class.

    print("\nProduction worker information")
    print("-" * 29)

    # Using getters from both classes to output information.
    print("Name: " + a.getName())
    print("Employee ID: " + a.getNum())
    print("Shift: " + b.getShiftNum())
    print("Hourly Pay Rate: ${:.2f}".format(b.getHourlyPay()))
    
    print("\nProduction worker information")

#-----------------------------------------------------------------------
# PROGRAM'S MAIN LOGIC
#

main()
input("\nRun complete. Press the Enter key to exit.")