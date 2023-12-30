# Write Program to remove duplicate elements in an array
n = int(input("Enter the size of array: "))
arr=[]

for i in range(0,n):
    m=int(input("Enter element"))
    arr.append(m)
    
print(list(set(arr)))