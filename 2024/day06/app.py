from fileinput import input

def itocoord(num):
    return (num % width, num // width)

def in_bounds(pos):
    x,y = pos
    return x>=0 and y >= 0 and x < width and y < height

def add(pos, d):
    newpos = tuple(map(sum, zip(pos, d)))
    return newpos if in_bounds(newpos) else False

def get_next(d):
    return turn[(turn.index(d) + 1) % len(turn)]

def traverse(guard, crates, curdir): 
    recorded = [guard]
    hadtoturn = []
    while True:
        newpos = add(guard, curdir)
        if not newpos:
            break

        bumped = False
        while newpos in crates:
            bumped = True
            curdir = get_next(curdir)
            newpos = add(guard, curdir)

        if bumped:
            if (newpos,curdir) in hadtoturn:
                return False
            hadtoturn += [(newpos,curdir)]

        recorded += [newpos]
        guard = newpos
    return recorded 

lines = [line.strip() for line in input()]
line = ''.join(lines)
width = len(lines[0])
height = len(lines)

crates = [itocoord(x) for x,char in enumerate(line) if char == "#"]
guard = itocoord(line.index("^"))

defdir = (0,-1)
turn = [(0,1),(-1,0),(0,-1),(1,0)]

recorded = traverse(guard,crates, defdir) 
print("part1", len(set(recorded)))
print("part2", sum([not traverse(guard,crates + [i],defdir) for i in set(recorded) if i != guard])) 

