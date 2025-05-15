N = int(input())
user = []

for _ in range(N):
    age, name = input().split()
    user.append((int(age), name))

user.sort()  # 기본적으로 age(0번째 요소) 기준으로 정렬된다

for age, name in user:
    print(age, name)



