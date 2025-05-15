import sys
input = sys.stdin.read

N = int(input())
list_a =[]
for i in range(N):
    a,b = map(int, input().split())
    list_a.append([a,b])
list_a.sort()
for i in range(N):
    print(list_a[i])
