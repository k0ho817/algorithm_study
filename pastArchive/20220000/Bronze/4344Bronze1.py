#평균은 넘겠지
x = int(input())
lst = []
lst1 = []
summary = int()
numPepole = 0
for i in range(0,x):
    a = list(map(int, input().split()))
    lst.append(a)
    summary += sum(a[1:])
    numPepole += a[0]

avg = summary / numPepole