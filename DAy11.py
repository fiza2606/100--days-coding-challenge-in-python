# Write a program to find Fibonacci series up to n
n = int(input("Enter a num to find fibonacci series: "))
a = 0
b = 1
sum = 0
print("Fibonacci Series : ", end = " ")
while(sum <= n):
     print(sum, end = " ")
     a = b
     b = sum
     sum = a + b

