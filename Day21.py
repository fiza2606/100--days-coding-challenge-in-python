# Write a program to identify if the number is Palindrome or not
num = int(input("Enter a number: "))
n = num
rev = 0
while num > 0:
    dig = num %10
    # taking the last digit
    rev = rev*10+dig
    #  appending last digit to rev variable
    num = num//10
    
if n == rev:
    print("Palindrome")
else:
    print("Not a palindrome")

    