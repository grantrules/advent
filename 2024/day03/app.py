from fileinput import input
import re

line = ''.join(input())
p = r"mul\((\d+),(\d+)\)"
rep = r"don\'t\(\).*?(do\(\)|$)"

def muls(l):
    return sum(int(x)*int(y) for x,y in re.findall(p, l))

print(muls(line))
print(muls(re.sub(rep, "", line, flags=re.DOTALL)))
exit()

from functools import reduce


p2 = r"(do\(\))|(don't\(\))|mul\((\d+),(\d+)\)"
print(re.findall(p2, line))
cmds = re.findall(p2, line)

isdo = True
total = 0
for do,dont,x,y in cmds:
    if do != '':
        isdo = True
    elif dont != '':
        isdo = False
    elif isdo:
        total += int(x) * int(y)
print(total)

def handle(a,x):
    do,dont,x,y = x
    todo, total = a
    return [todo if x != '' else do != '', total if not todo or x == '' else (total + int(x) * int(y))]

print(reduce(handle, cmds, (True,0)))
#def handle_input(line):
#    print("line:", line.strip())

#lines = list(map(handle_input, input()))



#for line in input():
#    numlist.append(list(map(int,line.split())))
