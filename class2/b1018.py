n, m = map(int, input().split())
board = [input() for _ in range(n)] # 한줄씩 입력 n 번만큼 받아서 리스트 로 만듬
min_count = 64

for row in range(n-7):
    for col in range(m-7):
        w_count = 0
        b_count = 0

        for i in range(8):
            for j in range(8):
                current = board[row + i][col + j] #현재 위치
                if (i + j) % 2 == 0:  # 짝수 칸
                    if current != 'W': # w 시작 보드는 짝수칸이 w, w가 아니면 w error count 1 증가
                        w_count += 1
                    if current != 'B':# b 시작 보드는 짝수칸이 b, b가 아니면 b error count 1 증가
                        b_count += 1
                else:  # 홀수 칸
                    if current != 'B':# w 시작 보드는 홀수칸이 b, b가 아니면 w error count 1 증가
                        w_count += 1
                    if current != 'W':# b 시작 보드는 홀수칸이 w, w가 아니면 b error count 1 증가
                        b_count += 1

        min_count = min(min_count,w_count, b_count)
print(min_count)



