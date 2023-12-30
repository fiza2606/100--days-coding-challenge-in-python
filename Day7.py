# Write a program to find Number of days in a given month of a given year
m = int(input("Enter month: "))
y = int(input("Enter year: "))
if ((y % 400==0 and y % 100==0) and m==2):
    print("29 days")
elif m==2:
    print("28 days")
elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    print("31 days")
else:
    print("30 days")
