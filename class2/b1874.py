N = int(input())
num_list = [int(input()) for _ in range(N)]

stack = []
current = 1
result = []

for num in num_list:
    while current <= num:
        stack.append(current)
        result.append("+")
        current += 1
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit()

print("\n".join(result))
