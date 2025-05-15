# 입력 받기
T = int(input())  # 테스트 케이스 개수

result = []

# 각 테스트 케이스 처리
for _ in range(T):
    # 반복 횟수와 문자열 분리
    R, S = input().split()
    R = int(R)

    # 새로운 문자열 P 생성
    P = ''
    for char in S:
        P += char * R  # 각 문자를 R번 반복하여 추가
    result.append(P)

# 최종 출력
print("\n".join(result))
