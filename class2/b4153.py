n_list = []
while True:
    nums = list(map(int, input().split()))
    if nums == [0,0,0]:
        break
    nums.sort()
    a,b,c = nums
    if a**2+b**2 == c**2:
        n_list.append("right")
    else:
        n_list.append("wrong")

for i in range(len(n_list)):
    print(n_list[i])
