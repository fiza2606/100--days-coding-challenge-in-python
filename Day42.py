# Write Program to check if two arrays are the same or not
def arrays(arr1, arr2, n1, n2):

    count = 0

    arr1.sort()

    arr2.sort()

    for i in range(0,n1):

        if(arr1[i] == arr2[i]):

            count = count + 1
    return count

 

n1 = int(input("Enter the size of first array: "))

n2 = int(input("Enter the size of second array: "))

arr1 = []

arr2 = []

print("Enter the elements of first array: ")

for i in range(0,n1):

    temp = int(input())

    arr1.append(temp)

print("Enter the elements of second array: ")

for i in range(0,n2):

    temp = int(input())

    arr2.append(temp)

 

if(arrays(arr1, arr2, n1, n2) != n1):

    print("Not Same")

else:

    print("Same")