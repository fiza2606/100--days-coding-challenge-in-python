# taking input from user
char = input("Enter any character from a-z:")
vowel = 'aeiouAEIOU' #defining all vowels in a variable
    
if char.isnumeric():      # to check whether input is number
    print("invalid input")
elif char in vowel:        
    print("vowel")
else:
    print("Consonant")
        
