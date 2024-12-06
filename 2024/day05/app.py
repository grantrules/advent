from fileinput import input
import random

def nums(l, char) -> list[int]:
    return list(map(int, l.strip().split(char)))

def wrong(p,x,y) -> bool:
    return x in p and y in p and p.index(x) > p.index(y)

def fix(p):
    for x,y in rules:
        if wrong(p,x,y):
            p[p.index(x)], p[p.index(y)] = y, x 
            return fix(p)
    return p

def get_middles(pages):
    return [p[len(p)//2] for p in pages]

lines = [line.strip() for line in input()]
rules = [nums(l, "|") for l in lines if "|" in l]
pages = [nums(l, ",") for l in lines if "," in l]

correct = [p for p in pages if not any([wrong(p,x,y) for x,y in rules])]
fixed = [fix(p) for p in pages if p not in correct]
        
print("part1:",sum(get_middles(correct)))
print("part2:",sum(get_middles(fixed)))
