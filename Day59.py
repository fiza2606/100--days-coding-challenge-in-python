# Body Mass index
n = int(input())
for i in range(n):
    m,h = map(int,input().split())
    bmi = m/(h*h)
    # print(bmi)
    if (bmi<=18):
        print(1)
    elif (19<=bmi<=29):
        print(2)
    elif (25<=bmi<=29):
        print(3)
    elif (30<=bmi):
        print(4)

