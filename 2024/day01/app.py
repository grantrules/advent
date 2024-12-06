from fileinput import input
from collections import Counter

a,b = zip(*[[int(n) for n in line.split()] for line in input()])
cnt = Counter(b)

print("part1", sum(abs(x - y) for x,y in zip(sorted(a),sorted(b))))
print("part2", sum([cnt[x] * x for x in a if cnt[x]]))
