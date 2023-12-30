#  Write a program to identify if the number is Prime number or not
num = int(input("Enter a number: "))
temp = 0
for i in range(2,num):
    if num % i ==0:
        temp+=1
if temp == 0:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")