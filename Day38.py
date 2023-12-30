# Write a Program to print Non-repeating characters in a string
s = input("Enter a string: ")
for i in s:
    count =0
    for j in s:
        if i==j:
            count+=1
        if count>1:
            break
    if count==1:
        print(i,end="")