N, M = map(int, input().split())
num = list(map(int, input().split()))
result = 0
flag = False
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            sum_c = num[i] + num[j] + num[k]
            if sum_c == M:
                result = M
                flag = True
                break
            elif result < sum_c < M:
                result = sum_c
        if flag:
            break
    if flag:
        break

print(result)