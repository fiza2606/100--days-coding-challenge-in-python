# Write a Program to Remove vowels from a string
s= input("Enter a string: ")
s1=""
vowels= ['a','e','i','o','u','A','E','I','O','U']
for i in s:
    if i not in vowels:
        s1=s1+i
print(s1)