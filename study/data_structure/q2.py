# 배열과 리스트
# 02 평균 구하기
# 시간 제한 : 2초 -> 4000만번
# 데이터 최대 크기 : 1000

# num에 입력
# num_list에 숫자리스트 입력
# max값 구하기
# 리스트에 있는 숫자 바꾸고 평균 구하기

# 처음 코드
# num = int(input())
# num_list = list(map(int, input().split()))
# max_num = max(num_list)

# for i in range(num):
#     num_list[i] = num_list[i] / max_num * 100

# print(sum(num_list)/num)


num = int(input())
num_list = list(map(int, input().split()))
max_num = max(num_list)
sum_result = sum(num_list)

# 한 과목과 관련된 수식을 총합한 후 관련 수식으로 변환해 로직을 간단하게 할 수 있음
print(sum_result/max_num*100/num)