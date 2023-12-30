# Balancing weight
a = int(input())
for i in range(a):
    w1,w2,x1,x2,m=list(map(int,input().split()))
    h= w2-w1
    s1=x1*m
    s2=x2*m
    if h>=s1 and h<=s2:
        print(1)
    else:
        print(0)