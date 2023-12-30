# Write Program to find whether the numbers of an array be made equal
def arrayEqual(arr):
    for i in range(0,len(arr)):
        while arr[i]%2 == 0:
            arr[i]//=2
        while arr[i]%3 == 0:
            arr[i]//=3
    for i in range(0,len(arr)):
        if arr[i]!= arr[0]:
            return False
    return True

# arr = list(map(int,input().split('')))
arr = list(map(int,input("Array : ").split(' ')))
if arrayEqual(arr) == True:
    print("Yes")
else:
    print("No")