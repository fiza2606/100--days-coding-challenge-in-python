# Given an integer array of size N, write a program to reverse the array;
n = int(input("Enter the size of array: "))
arr=[]

for i in range(0,n):
    m=int(input("Enter elements: "))
    arr.append(m)
arr.reverse()
print(arr)