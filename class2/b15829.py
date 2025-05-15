n = (input())
r = 31
m = 1234567891
power = 0
hashing = 0

origin = input()
for c in origin:
    hashing = (hashing+(ord(c)-96)*power%m)
    power = (power*r) % m
print(hashing)

