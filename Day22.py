# Write a program to express a number as a sum of two prime numbers
num = int(input("Enter the number: "))
arr=[]
for i in range(2,num):
    flag =0
    for j in range(2,i):
        if (i % j == 0):
            flag =1
    if (flag == 0):
        arr.append(i)
        print(arr)

flag =0        
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if (arr[i]+arr[j]== num):
            flag=1
            print(num,"can be expressed as sum of",str(arr[i]),"and",str(arr[j]))
            break
if (flag==0):
    print("No prime number can give sum of " + str(num))


        
        