# Write a Program to calculate the Frequency of characters in a string
s=input("Enter a string: ")
for i in s:
    freq= s.count(i)
    print("frequency of "+str(i)+" is "+str(freq), end="\n")