people = int(input())
size = list(map(int, input().split()))
T,P = map(int, input().split())
t_count = 0
p_count = 0
p_ea_count = 0
for s in size:
    if s%T == 0:
        t_count += s//T
    else:
        t_count += (s//T)+1
p_count = people//P
p_ea_count = people%P
print(t_count)
print(p_count,p_ea_count)
