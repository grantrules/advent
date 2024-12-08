from fileinput import input

def get_all(arr, length):
    for i in range(0, len(arr) ** length):
        res = int_to_perm(arr,i)
        yield res + [arr[0] for i in range(0,length - len(res))]

def int_to_perm(arr, num):
    res = []
    while num > 0:
        res += [arr[num % len(arr)]]
        num //= len(arr) 
    return res

def check(value, nums, o):
    total = nums[0]
    for i,op in enumerate(o):
        total = op(total,nums[i+1])
    return value == total


def is_valid(value, nums, ops):
    o = list(get_all(ops, len(nums)-1))
    return any([check(value, nums,oplist) for oplist in o])

ops = [lambda a,b: a+b, lambda a,b: a*b]

lines = [line.strip().split(":") for line in input()]
m = [(int(x),list(map(int,y.split()))) for x,y in lines] 

total = sum([x for x,y in m if is_valid(x,y,ops)])
print("part1", total)
total2 = sum([x for x,y in m if is_valid(x,y,ops + [lambda a,b: int(str(a) + str(b))])])
print("part2", total2)

