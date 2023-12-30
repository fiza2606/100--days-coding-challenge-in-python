# Write Program to find number of even and odd elements in an array
n = int(input("Enter the size of array: "))
arr=[]
e=0
o=0
for i in range(0,n):
    m=int(input("enter the elements: "))
    arr.append(m)
for j in range(0,n):
    if arr[j]% 2==0:
        e=e+1
    else:
        o=o+1
print("Number of even elements: ",e)
print("Number of odd elements:",o)