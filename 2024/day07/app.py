from fileinput import input


def get_all(arr, length):
    for i in range(0, len(arr) ** length):
        yield (res := int_to_perm(arr,i)) + [arr[0]] * (length - len(res))

def int_to_perm(arr, num):
    return [] if num == 0 else \
        [arr[num % len(arr)]] + int_to_perm(arr, num // len(arr))

def check(value, nums, o):
    total = nums[0]
    for i,op in enumerate(o):
        total = op(total,nums[i+1])
    return value == total

def is_valid(value, nums, ops):
    return any([check(value, nums, oplist) for oplist in get_all(ops, len(nums)-1)])

ops = [lambda a,b: a+b, lambda a,b: a*b]

lines = [line.strip().split(":") for line in input()]
m = [(int(x),list(map(int,y.split()))) for x,y in lines] 

total = sum([x for x,y in m if is_valid(x,y,ops)])
print("part1", total)
total2 = sum([x for x,y in m if is_valid(x,y,ops + [lambda a,b: int(str(a) + str(b))])])
print("part2", total2)

