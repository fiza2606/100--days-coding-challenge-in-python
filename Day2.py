# Write a program to identify if the character is an alphabet or not.
char = input("Enter any input character: ")
if char.isalpha(): # isalpha() is string method to check whether the alphabet is character or not
    print("Alphabet")
else:
    print("Not an alphabet")