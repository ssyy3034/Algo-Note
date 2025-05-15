grade = input().strip()  # 예: A+, B0, C-, F 등

score = 0.0

if grade == 'F':
    score = 0.0
else:
    if grade[0] == 'A':
        score = 4.0
    elif grade[0] == 'B':
        score = 3.0
    elif grade[0] == 'C':
        score = 2.0
    elif grade[0] == 'D':
        score = 1.0

    if len(grade) == 2:  # 부호가 있는 경우
        if grade[1] == '+':
            score += 0.3
        elif grade[1] == '-':
            score -= 0.3

print(score)
