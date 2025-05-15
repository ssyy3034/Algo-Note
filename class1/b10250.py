testcase = int(input())
room_num = []

for _ in range(testcase):
    H, W, N = map(int, input().strip().split())

    floor = N % H
    room = N // H + 1

    if floor == 0:
        floor = H
        room -= 1

    room_num.append(f"{floor}{room:02d}")

for num in room_num:
    print(num)
