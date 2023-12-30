# Write a Program to check if two strings are Anagram or not
s = input("Enter string: ")
rev= str(s)[::-1]
if s==rev:
    print("Anagram")
else:
    print("Not a anagram")