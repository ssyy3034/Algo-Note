N = int(input())

room = 1  # 방 개수 누적
layer = 1  # 층 수 (거리)

while N > room:
    room += 6 * layer  # 다음 층까지 방 개수 추가
    layer += 1

print(layer)


