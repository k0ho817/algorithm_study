#숫자의 합
a = int(input())
b = str(input())
c = int(b[0])

for i in range(1,a):
    c += int(b[i])

print(c)