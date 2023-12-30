# Gold Mining
a= int(input())
for i in range(a):
    n,x,y = list(map(int,input().split()))
    if x>y:
        print("no")
    else:
        print("Yes")