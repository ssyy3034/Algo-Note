S = input().strip()
result = 0

phone_dict = {
    "ABC":3,
    "DEF":4,
    "GHI":5,
    "JKL":6,
    "MNO":7,
    "PQRS":8,
    "TUV":9,
    "WXYZ":10
}
for s in S:
    for key in phone_dict.keys():
        if s in key:
            result += phone_dict[key]
            break
print(result)


