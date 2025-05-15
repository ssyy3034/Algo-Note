import itertools

n = int(input())
p = map(int,input().split())
p = sorted(p)
totalTime = 0
p = list(itertools.accumulate(p))
for time in p:
    totalTime += time
print(totalTime)

