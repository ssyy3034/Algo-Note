s = input()
result = ""

for char in s:
    if char.islower():
        result += char.upper()
    elif char.isupper():
        result += char.lower()
    else:
        result += char  # 숫자, 공백 등은 그대로

print(result)
