# Given 2 integer arrays X and Y of same size. Consider both arrays as vectors and print the sum of maximum scalar product (Dot product) of 2 vectors.
def scalarProduct(arr1,arr2):
    p=0
    arr1.sort()
    arr2.sort()
    for i in range(0,len(arr1)):
        p=p+arr1[i]*arr2[i]
        print(arr1[i],"*",arr2[i],"=",p)    
    return p


arr1 = list(map(int,input("Array 1: ").split(' ')))
arr2 = list(map(int,input("Array 2: ").split(' ')))
print(scalarProduct(arr1,arr2)) 