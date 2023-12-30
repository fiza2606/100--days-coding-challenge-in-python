# Good weather
n = int(input())

for i in range(n):
    a = list(map(int,input().split()))
    b = 7
    x=a.count(0)
    y=a.count(1)
    if x>y:
        print("No")
    else:
        print("Yes")
    