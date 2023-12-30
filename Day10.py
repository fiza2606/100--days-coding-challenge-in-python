# Write a program to find Factorial of a number
n = int(input("Enter any num to find factorial: "))
fact = 1
if n < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif n == 0:
   print("The factorial of 0 is 1")
else:
    for i in range(1,n+1):
        fact = fact*i
print(fact)