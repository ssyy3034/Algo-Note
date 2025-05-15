n, m = map(int, input().split())
rope_list = [int(input()) for _ in range(n)]

result = 0
start = 1
end = max(rope_list)

while start <= end:
    mid = (start + end) // 2
    count = sum(length // mid for length in rope_list)

    if count >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1  # ✅ 여기!

print(result)
