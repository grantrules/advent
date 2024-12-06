from fileinput import input
from functools import reduce
DIRS = {
    "^": (0, 1),
    ">": (1, 0),
    "v": (0, -1),
    "<": (-1, 0),

}

path = ''.join(input()).strip()
home = (0,0)
print(len(set(reduce(lambda a, h: a+ [tuple(map(sum,zip(a[-1], DIRS[h])))], path, [(0,0)]))))

print(len(set(reduce(lambda a,h: a+ [tuple(map(sum,zip(a[-1], DIRS[h])))], map(lambda x: path[x], range(0,len(path),2)), [(0,0)]) + reduce(lambda a,h: a+ [tuple(map(sum,zip(a[-1], DIRS[h])))], map(lambda x: path[x], range(1,len(path),2)), [(0,0)]) )))
#print(list(map(lambda h: tuple(map(sum,zip(home, DIRS[h]))) ,path)))
