# Write a program to find Sum of digits of a number
n = int(input("Enter any number: "))
sum =0
for digit in str(n):
    sum+= int(digit)
print(sum)