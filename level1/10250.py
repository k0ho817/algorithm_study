# ACM 호텔

lst = []
dataNum = int(input())
for i in range(dataNum):
    lst.append(list(map(int, input().split())))

for j in lst:
    floor = j[2] % j[0]
    room = j[2] // j[0] + 1

    if floor == 0:
        floor = j[0]
        room -= 1
    
    result = str(floor) + '{0:0>2}'.format(room)
    print(result)