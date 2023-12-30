# Given an integer array of size N, write a program to sort the array;
n = int(input("Enter the size of array: "))
arr=[]

for i in range(0,n):
    m=int(input("Enter element for X: "))
    arr.append(m)
arr.sort()
print(arr)