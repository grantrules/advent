import fileinput

for line in fileinput.input():
    total = 0
    for i,c in enumerate(line):
        total += 1 if c == "(" else -1
        if total < 0:
            print(i+1)
            break

