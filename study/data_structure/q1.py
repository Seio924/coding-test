# 배열과 리스트
# 01 숫자의 합 구하기
# 시간제한 : 1초 -> 2000만번
# 데이터 최대 크기 : 100

num = int(input())
num_list = list(input())
sum_result = 0

for i in range(num):
    sum_result += int(num_list[i])

print(sum_result)