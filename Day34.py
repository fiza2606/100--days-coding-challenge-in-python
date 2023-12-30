# Write a Program to Remove brackets from an algebraic expression
s= input("Enter an expression: ")
b=['(',')','[',']','{','}']
str=""
for i in s:
    if i not in b:
        str=str+i
print(str)