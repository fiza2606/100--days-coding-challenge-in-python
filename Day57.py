# "Pass or Fail
a = int(input())
for i in range(a):
    n,x,p = list(map(int,input().split()))
    g = n-x
    if ((x*3)-g)>=p:
        print("Pass")
    else:
        print("Fail")
    