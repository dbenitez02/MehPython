#-----------------------------------------------------------------------
# Program name: Assignment7.py
# Author: Daniel Benitez
# Date:
# Purpose: Simulate a radio tuner
#-----------------------------------------------------------------------
# GLOBAL VARIABLE DEFINITIONS (Use only until functions)

# Variable Type: Variable list separated by commas

#-----------------------------------------------------------------------
# CONSTANT DEFINITIONS

#-----------------------------------------------------------------------
# CLASS DEFINITIONS
class Radio:
    stations = ["STATIC", "97.2", "99.6", "101.7", "105.3", "108.5"]

    # Initiating the class and private variables
    def __init__(self):
        self.i = 0
        self.radioPresets = ["STATIC"] * 3

    def seekNext(self):
        self.i += 1
        self.stations[self.i]
        print("Current radio station: {}\n".format(self.stations[self.i]))

    def longPressPreset1(self):
        self.preset1 = self.stations[self.i]
        self.radioPresets[0] = self.stations[self.i]
        
    def longPressPreset2(self):
        self.preset2 = self.stations[self.i]
        self.radioPresets[1] = self.stations[self.i]

    def longPressPreset3(self):
        self.preset3 = self.stations[self.i]
        self.radioPresets[2] = self.stations[self.i]
    
    def shortPressPreset1(self):
        self.i = self.stations.index(self.preset1)

    def shortPressPreset2(self):
        self.i = self.stations.index(self.preset2)
    
    def shortPressPreset3(self):
        self.i = self.stations.index(self.preset3)

    def displayLCD(self):
        print("current radio station: {}\n".format(self.stations[self.i]))

    def __str__(self):
       return "Preset 1: {}\nPreset 2: {}\nPreset 3: {}\n".format(*self.radioPresets)


#-----------------------------------------------------------------------
# FUNCTION DEFINITIONS

def main():
    displayMenuGetOption()


def displayMenuGetOption():

    personalStation = Radio()
    print("\n")

    while True:

        print("1 = Display tuned in station")
        print("2 = Program preset station 1")
        print("3 = Program preset station 2")
        print("4 = Program preset station 3")
        print("5 = Seek next station")
        print("6 = Tune preset station 1")
        print("7 = Tune preset station 2")
        print("8 = Tune preset station 3")
        print("9 = Dump Programming")
        print("10 = Turn off radio\n")

        option = str(input("Enter option: "))
        print("\n")

        if option == '1':
           personalStation.displayLCD()
           
        elif option == '2':
            personalStation.longPressPreset1()

        elif option == '3':
            personalStation.longPressPreset2()

        elif option == '4':
            personalStation.longPressPreset3()

        elif option == '5':
            personalStation.seekNext()

        elif option == '6':
            personalStation.shortPressPreset1()
            personalStation.displayLCD()

        elif option == '7':
            personalStation.shortPressPreset2()
            personalStation.displayLCD()

        elif option == '8':
            personalStation.shortPressPreset3()
            personalStation.displayLCD()

        elif option == '9':
            print(personalStation.__str__())
            personalStation.displayLCD()

        elif option == '10':
            break    
#-----------------------------------------------------------------------
# PROGRAM'S MAIN LOGIC
#

main()
input("Run complete. Press the Enter key to exit.")