# 구간 합
# 03 구간 합 구하기2
# 시간 제한 : 1초 -> 2000만번 (20,000,000)
# 데이터 최대 크기 : 1024


# 배열 크기, 질문 개수 입력

# 구간합 배열 가장자리 0

# for 배열 크기:
#     배열에 한줄로 입력한 배열 추가

# for 1~배열크기+1:
#     for 1~배열크기+1:
#         D[i][j] = D[i-1][j] + D[i][j-1] + N[i-1][j-1] - D[i-1][j-1]

# D[2번째 좌표] - D[첫번째 좌표]


import sys

input = sys.stdin.readline

size, q_num = map(int, input().split())

N = []
D = [ [0 for _ in range(size+1)] for _ in range(size+1)]

for _ in range(size):
    N.append(list(map(int, input().split())))


for i in range(1, size+1):
    for j in range(1, size+1):
        D[i][j] = D[i-1][j] + D[i][j-1] + N[i-1][j-1] - D[i-1][j-1]

for _ in range(q_num):
    x1, y1, x2, y2 = map(int, input().split())
    print(D[x2][y2] - D[x1][y1])