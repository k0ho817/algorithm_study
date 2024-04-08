#2007년
m, d = map(int, input().split())
day = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
a = [0,31,28,31,30,31,30,31,31,30,31,30]
date = (sum(a[0:m]) + d) % 7 - 1
print(day[date])