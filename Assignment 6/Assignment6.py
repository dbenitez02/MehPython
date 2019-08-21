import pickle
#-----------------------------------------------------------------------
# Program name: File Encryption
# Author: Daniel Benitez
# Date: 
# Purpose: Encrypt and decrypt an exisiting file.
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# FUNCTION DEFINITIONS

def main():
    
    return input("\nRun complete. Press the Enter key to exit.")

def displayMenuAndGetOption():
    print("FILE ENCRYPTION PROGRAM\n")

    print("E = Encrypt a file")
    print("D = Decrypt a file")
    print("Q = Quit the program\n")
    
    userInput = str(input("Enter menu selection (E, D, or Q): ")).capitalize()

    while True:
        
        if userInput == 'E':
            fileEncrypt = str(input("Enter the file to ENCRYPT. Press Enter alone to abort: "))

            if fileEncrypt == '':
                break
            else:
                getFiles(fileEncrypt)
            break

        elif userInput == 'D':
            fileDecrypt = str(input("Enter the file to DECRYPT. Press Enter alone to abort: "))

            if fileDecrypt == '':
                break
            else:
                getFiles(fileDecrypt)
            break

        elif userInput == 'Q':
            False
        else:
            return print("\nError - Invalid option.")
            False

def getFiles(a):

    try:
        # Check if the file to encrypt exists.
        f = open(a, "r")
    except IOError:
        # If file does not exist, try again.
        print("Error - that file does not exist. Try again.")
        main()
    
    fileOutput = str(input("Enter the output file name: "))
    g = open(fileOutput, "w")
    convert(f, g)


        
    

def convert(inputFile, outputFile):
    n = ''

    # Encryption and decryption are inverse of one another
    CODE = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\
            'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
            'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
            'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
            'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
            'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\
            'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\
            'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
            'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
            '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
            '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
            '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
            ':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
            "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
            '{':'[','[':'{','}':']',']':'}'}

    newlist = list(inputFile)
    print(newlist)
    # Individualy iterate through each character and endcode.
    for i in newlist:
        for j in i:
            if j in CODE:
                outputFile.write(CODE[j])

    
    
    
    

#-----------------------------------------------------------------------
# PROGRAM'S MAIN LOGIC
#

displayMenuAndGetOption()
main()

