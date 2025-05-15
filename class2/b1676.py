N = int(input())
facto = 1
zero_count = 0
while N > 0:
    facto *= N
    N -= 1
facto = str(facto)
for c in facto[::-1]:
    if c == "0":
        zero_count += 1
    else:
        break

print(zero_count)
