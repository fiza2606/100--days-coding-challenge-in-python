# Write a program to find the Quadrants in which coordinates lie
x = int(input("Enter the value for x : "))
y = int(input("Enter the value for y: "))
if (x>0 and y>0):
    print("This point lies in first quadrant.")
elif (x<0 and y>0):
    print("This point lies in second quadrant.")
elif (x<0 and y<0):
    print("This point lies in third quadrant.")
else:
    print("This point lies in fourth quadrant.")