'''
1~10
1 //
2 바닥
3 //
4 바닥
5 //
6 바닥
7 //
8 바닥
9 //
10 바닥
2 //
4 바닥
6 //
8 바닥
10 //
4 //
8 바닥
리스트 두개로 old,new 나눠서 old에서 new로 보낼때 바닥 연산
if len(new) == 1 이면 print
'''
from collections import deque

N = int(input())
queue = deque(range(1, N + 1))

while len(queue) > 1:
    # 첫 번째 카드 버림
    queue.popleft()

    # 두 번째 카드를 맨 뒤로 보냄
    queue.append(queue.popleft())

print(queue[0])


