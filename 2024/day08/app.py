from fileinput import input
from collections import defaultdict
import itertools


def dif(a,b):
    return tuple(map(lambda x: abs(x[0] - x[1]), zip(a,b)))

def add(a,b):
    return tuple(map(lambda x: x[0] + x[1], zip(a,b)))

def sub(a,b):
    return tuple(map(lambda x: x[0] - x[1], zip(a,b)))

def in_bounds(lines, pos):
    x,y = pos
    return x >= 0 and x < len(lines[0]) and y >= 0 and y < len(lines)

lines = [l.strip() for l in input()]
line = ''.join(lines) 
length = len(lines[0])

antennas = defaultdict(list)
a = [[char, (n%length,n//length)] for n,char in enumerate(line) if char != "."]
for char,pos in a:
    antennas[char].append(pos)


antis = []
p2 = []
for char in antennas: 
    combos = itertools.combinations(antennas[char],2)
    for a,b in combos:
        d = sub(a,b)
        print(a,b,d)
        if add(max(a,b),d) not in [a,b]:
            pos = add(max(a,b),d)
            while in_bounds(lines, pos):
                print("a", pos)
                p2 += [pos]
                pos = add(pos, d)
        else:
            pos = sub(max(a,b),d)
            while in_bounds(lines, pos):
                print("b", pos)
                p2 += [pos]
                pos = sub(pos,d)
        if sub(min(a,b),d) not in [a,b]:
            pos = sub(min(a,b),d)
            while in_bounds(lines, pos):
                print("c", pos)
                p2 += [pos]
                pos = sub(pos, d)
        else:
            pos = add(min(a,b),d)
            while in_bounds(lines, pos):
                print("d", pos)
                p2 += [pos]
                pos = add(pos,d)

        added = add(max(a,b),d) if add(max(a,b),d) not in [a,b] else sub(max(a,b),d) 
        subed = sub(min(a,b),d) if sub(min(a,b),d) not in [a,b] else add(min(a,b),d)
        print(added, in_bounds(lines, added))
        print(added, subed, in_bounds(lines, added), in_bounds(lines, subed))
        if in_bounds(lines, added):
            antis += [added]
        if in_bounds(lines, subed):
            antis += [subed]
for char in antennas:
    if len(antennas[char]) > 1:
        p2 += antennas[char]
print(antennas)
print("part1", len(set(antis)))
print(antis)
for i,l in enumerate(lines):
    s = ""
    for j,c in enumerate(l):
        #print(j,i, (j,i) in antis)
        s += "#" if (j,i) in p2 else c
    print(s)
print("part2",len(set(p2)))
