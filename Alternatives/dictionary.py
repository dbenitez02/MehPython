# Another, better variation of Assignment 3.
# This utilizes dictionaries rather then using if-else statments.

def zippy(n):
    zipcode = { "93305": "Your polling station is 123 Panorama Drive.",
                "93306": "Your polling station is 6143 Fairfax Drive.",
                "93307": "Your polling station is 21121 B Street.",
                "93308": "Your polling station is 863 Desmond Ct.",
                "93309": "Your polling station is 7332 Del Canto Ct." }
    
    for i in zipcode:
        if n in zipcode:
            print(zipcode[n])
            break
        else:
            print("Oopsie")
            break
    



# -- main code--
age = 1
while age != 0:
    age = int(input("Enter your age: "))
    
    if age == 0:
        print("Program has ended")
    elif age < 18:
        print("Not old enough.. newbie")
    elif age >= 18:
        num = input("Enter your zipcode: ")
        zippy(num)
