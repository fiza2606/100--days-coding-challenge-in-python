import math
a = int(input('Enter value for a :'))
b = int(input('Enter value for b :'))
c = int(input('Enter value for c :'))
if a == 0:
 print("a cannot be zero")
else:
 d = b**2 - 4 * a * c
 root = math.sqrt(abs(d))
 
if d > 0:
    print("Two Real Roots")
    print((-b + root)/(2 * a))
    print((-b -root)/(2 * a))
elif d == 0:
    print("Roots are equal")
    print(-b / (2*a))
 
else:
    print("No Real Root")
    print(- b / (2*a) , " + i", root)
    print(- b / (2*a) , " - i", root)