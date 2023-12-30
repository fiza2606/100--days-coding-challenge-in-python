#  Write Program to find smallest and largest element in an arrayarr=[]
n = int(input("Enter the size of array: "))
arr=[]

for i in range(0,n):
    m=int(input("enter the elements: "))
    arr.append(m)
arr.sort()
print("Smallest Number: ",arr[0])
print("Largest Number:",arr[-1])