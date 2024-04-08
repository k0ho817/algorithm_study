# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

a = input().lower()
lst = []
alphabetList=[]
for i in range(97,123):
    alphabetList.append(chr(i))
for i in alphabetList:
    lst.append(a.count(i))
maxIdx = 0
for i in lst:
    if i == max(lst):
        maxIdx += 1
if (maxIdx != 1):
    print("?")
else:
    print(alphabetList[lst.index(max(lst))].upper())
