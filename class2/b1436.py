n = int(input())
numbers = []
t = 0
while len(numbers) < n:
    if "666" in str(t):
        numbers.append(t)
        t += 1
    else:
        t += 1
print(numbers[-1])