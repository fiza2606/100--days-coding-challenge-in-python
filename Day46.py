# Write Program to find sum of elements in an array
n = int(input("Enter the size of array: "))
arr=[]
count=0
for i in range(0,n):
    m=int(input("enter the elements: "))
    arr.append(m)
for j in range(0,n):
    count=arr[j]+count
print(count)
     