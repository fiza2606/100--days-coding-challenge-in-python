# Given an integer array of size N. Write Program to find sum of positive square elements in the array.
def sum(arr):
    sum=0 
    arr1=[]
    arr2=[]
   
    for j in range(0,len(arr)):
        arr1.append(arr[j]*arr[j]) 
    
    for x in arr1:
        if x not in arr2:
            arr2.append(x)
    for i in range(0,len(arr2)):
        sum=sum+arr2[i]

    return sum


arr = list(map(int,input().split(' ')))
print(sum(arr))