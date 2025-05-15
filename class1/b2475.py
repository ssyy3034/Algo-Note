S = input().split()
auth = 0
for s in range(len(S)):
    auth += int(S[s])*int(S[s])
auth = auth % 10
print(auth)