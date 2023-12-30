# Write a program to find the Factors of a number
num = int(input("Enter number to find factors: "))
for i in range(1,num+1):
    if num % i ==0:
        print(i)