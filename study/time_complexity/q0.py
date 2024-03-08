"""
수 정렬하기
시간 제한 : 2초 ( 1초당 2000만 번 )
데이터 최대 크기 : 1,000,000

4000만 번 이하의 연산 횟수로 해결해야 함
"""

num = int(input())
l = []

for i in range(num):
    l.append(int(input()))

l.sort()

for i in l:
    print(i)