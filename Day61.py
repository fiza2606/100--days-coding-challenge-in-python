# chess format
n = int(input())
for i in range(n):
    a,b = list(map(int,input().split()))
    if a+b<3:
        print(1)
    elif 3<=a+b<=10:
        print(2)
    elif 11<=a+b<=60:
        print(3)
    elif 60<a+b:
        print(4)