import string

# 입력 받기
S = input()

# 알파벳 리스트 초기화
alphabet = list(string.ascii_lowercase)

# 결과 리스트 초기화 (-1로 초기 설정)
result = [-1] * 26

# 문자열 순회
for index, char in enumerate(S):
    # 처음 등장한 문자일 경우 위치 저장
    if result[ord(char) - ord('a')] == -1:
        result[ord(char) - ord('a')] = index

# 결과 출력
print(" ".join(map(str, result)))
