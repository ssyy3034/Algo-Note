lines = []

try:
    while True:
        line = input()
        lines.append(line)
except EOFError:
    pass

for line in lines:
    print(line)
