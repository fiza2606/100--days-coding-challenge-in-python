# Write a program to print Pyramid pattern using stars
n = int(input("Enter the number: "))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print("\n")