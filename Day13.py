# Write a program to find Sum of N natural numbers
n = int(input("enter any number to find sum: "))
sum =0
while n>0:
    sum+=n
    n-=1
print(sum)