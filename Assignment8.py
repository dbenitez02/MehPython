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

class ProductionWorker(Employee):
    # Initiate ProductionWorker class under Employee class.
    # Store Shift number and Pay rate.
    def __init__(self, employeeName, employeeNum, shiftNum, hourlyPay):
        Employee.__init__(self, employeeName, employeeNum)

        self.__shiftNum = shiftNum
        self.__hourlyPay = float(hourlyPay)
    
    def getShiftNum(self):
        shift = self.__shiftNum
        return shift

    def getHourlyPay(self):
        pay = self.__hourlyPay
        return pay

    def __str__(self):
        output = "Employee Name: " + Employee.getName(self)
        output += "\nEmployee Number: " + Employee.getNum(self)
        output += "\nShift: " + self.__shiftNum
        output += "\nHourly Pay Rate: ${:.2f}".format(self.__hourlyPay) 
        return output
#-----------------------------------------------------------------------
# FUNCTION DEFINITIONS

def main():
    name = input("Enter the Name: ")
    employeeID = input("Enter the ID number: ")
    shiftNum = input("Enter Shift Number: ")
    hourlyPay = input("Enter Pay Rate: ")

    # Store input
    y = ProductionWorker(name, employeeID, shiftNum, hourlyPay)
    
    # Dump class info
    print("\nProduction worker information")
    print("-" * 28)
    print(y)

main()
input("\nRun complete. Press the Enter key to exit.")