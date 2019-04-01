import re

def pal(word):
    word.lower()
    first = 0
    last = len(word) - 1

    # Loop while the first position is less than the last position
    # Start from both ends of the word.
    while (first < last):

        # Both condition statements check for white spaces
        if re.search("\W", word[first]):
            first += 1
        if re.search("\W", word[last]):
            last -= 1
        
        # returns false if two letters done match
        if word[first] != word[last]:
            return print(word + " is not a palindrome")
        
        first += 1
        last -= 1

# ---Main code---
pal(input("Enter a word: "))