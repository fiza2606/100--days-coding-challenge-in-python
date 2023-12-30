#  Write a Program to Count the sum of numbers in a string
s = input("Enter the string: ")
sum=0

for i in s:
    if ord(i)>=48 and ord(i)<=57:
        sum=sum+int(i)
print(str(sum))