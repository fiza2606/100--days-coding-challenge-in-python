#  Write Program to find the array type
n = int(input("Enter the size of array: "))
arr=[]
for i in range(0,n):
    no = int(input("Enter the element: "))
    arr.append(no)

e=0
o=0
for j in range(n):
    if arr[j]%2==1:
        o=o+1
    else:
        e=e+1
if(o==n):
    print("Odd")
elif(e==n):
    print("Even")
else:
    print("mixed type")