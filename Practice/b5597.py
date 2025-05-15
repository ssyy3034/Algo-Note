
# 1부터 29까지 숫자를 가진 리스트 생성 (30은 제외)
check = list(range(1, 31))

for _ in range(28):
    # 한 줄씩 숫자 입력받기
    n = int(input())
    # 입력받은 번호가 check 리스트에 있으면 제거
    if n in check:
        check.remove(n)

check.sort()
# 남아 있는 수를 출력 (출석하지 않은 번호)
for missing in check:
    print(missing)
