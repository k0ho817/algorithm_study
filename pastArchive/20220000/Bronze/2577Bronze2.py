#숫자의 개수
a = int(input())
b = int(input())
c = int(input())

rslt = str(a * b * c)

count = [0,0,0,0,0,0,0,0,0,0]

for i in range(0,len(rslt)):
    for z in range(0,10):
        if int(rslt[i]) == z:
            count[z] += 1

for i in range(0,10):
    print(count[i])