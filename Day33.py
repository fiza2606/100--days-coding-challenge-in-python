# Write a Program to check if String is a palindrome or not
s= input("Enter a string: ")
str=""
for i in s:
    str= i+str
if str==s:
    print("Palindrome")
else:
    print("Not a palindrome")