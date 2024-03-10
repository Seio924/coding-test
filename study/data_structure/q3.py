# 구간 합
# 03 구간 합 구하기1
# 시간 제한 : 0.5초 -> 1000만번 (10,000,000)
# 데이터 최대 크기 : 100,000


# 데이터 개수, 반복 횟수 입력
# 숫자 리스트 입력
# 구간합 계산
# 구간 입력
# { 슈도코드 더 자세하게 적기 }

import sys

input = sys.stdin.readline

data_num, sum_num = map(int, input().split())
num_list = list(map(int, input().split()))
sum_list = [0]
tmp = 0

for i in num_list:
    tmp += i
    sum_list.append(tmp)

for i in range(sum_num):
    x, y = map(int, input().split())
    print(sum_list[y]-sum_list[x-1])