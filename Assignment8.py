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
    
    def __init__(self, employeeName, employeeNum):
        self.__employeeName = employeeName
        self.__employeeNum = employeeNum
    
    def getName(self):
        return self.__employeeName
    
    def getNum(self):
        return self.__employeeNum
    
    def __str__(self):
        output = "Name: " + self.__employeeName + "\n"
        output += "Employee ID: " + self.__employeeNum
        return output

# ProductionWorker inherits employeeName and employeeNum from the Employee class.
class ProductionWorker(Employee):

    def __init__(self, employeeName, employeeNum, shiftNum, hourlyPay):
        # Inherit the Employee class.
        Employee.__init__(self, employeeName, employeeNum)        
        
        self.__employeeName = employeeName
        self.__employeeNum = employeeNum
        self.__shiftNum = shiftNum
        self.__hourlyPay = float(hourlyPay)
    
    def getShiftNum(self):
        return self.__shiftNum

    def getHourlyPay(self):
        return self.__hourlyPay

    def __str__(self):
        output = "Name: " + self.__employeeName + "\n"
        output += "Employee ID: " + self.__employeeNum
        output += "\nShift: " + self.__shiftNum + "\n"
        output += "Hourly Pay Rate: ${:.2f}".format(self.__hourlyPay) 
        return output
#-----------------------------------------------------------------------
# FUNCTION DEFINITIONS

def main():
    name = input("Enter the Name: ")
    employeeID = input("Enter the ID number: ")
    shiftNum = input("Enter Shift Number: ")
    hourlyPay = input("Enter Pay Rate: ")

    y = ProductionWorker(name, employeeID, shiftNum, hourlyPay)
    
    print("\nProduction worker information")
    print("-" * 29)
    print(y)

#-----------------------------------------------------------------------
# PROGRAM'S MAIN LOGIC
#

main()
input("\nRun complete. Press the Enter key to exit.")