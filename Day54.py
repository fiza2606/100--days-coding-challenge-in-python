# Given an integer array of size N. Write Program to find whether Arrays are disjoint or not. Two arrays are said to be disjoint if they have no elements in common.

l1=set(map(int,input("Enter array1 ").split()))
l2=set(map(int,input("Enter array2 ").split()))
if(l1.intersection(l2)):
    print("Not a disjoint ")
else:
    print("disjoint")

