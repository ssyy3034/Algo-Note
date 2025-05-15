import numpy as np

n, m = map(int, input().split())

# A 행렬 입력
listA = [list(map(int, input().split())) for _ in range(n)]
# B 행렬 입력
listB = [list(map(int, input().split())) for _ in range(n)]

# numpy 배열로 변환
A = np.array(listA)
B = np.array(listB)

# 행렬 덧셈
sumAB = A + B

# 출력
for row in sumAB:
    print(*row)
