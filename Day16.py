# Write a program to identify if the number is Perfect number or not
num = int(input("Enter a number: "))
sum =0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if sum==num:
    print("Perfect number")
else:
    print("Not a perfect number")