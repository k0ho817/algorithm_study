#평균
a = int(input())
score = list(map(int, input().split()))
result = []
for i in range(0,a):
    result.append(score[i]/max(score)*100)
print(sum(result)/len(result))