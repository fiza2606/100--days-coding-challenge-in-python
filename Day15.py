# Write a program to identify if the number is Strong number or not
n= int(input("Enter any number: "))
sum =0 
temp=n
while(n):
    i=1
    fact=1
    rem= n%10
    while(i<=rem):
        fact = fact*i
        i=i+1
    sum = sum+fact
    n=n//10
if sum==temp:
    print("Strong number")
else:
    print("Not a strong number")