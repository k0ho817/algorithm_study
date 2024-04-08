a, b = map(int, input().split())
m = int(input())
sum = (b + m) // 60

if (a + sum) >= 24:
    a = a + sum - 24
else:
    a = a + sum

print(a, (b + m)%60)