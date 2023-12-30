# Write a Program to Capitalize the first and last letter of each word of a string
s = input("Enter a string: ")
str=s[0:1].upper() +s[1:len(s)-1] +s[len(s)-1:len(s)].upper()
print(str)
