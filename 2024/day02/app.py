from fileinput import input

numlist = [list(map(int,line.split())) for line in input()]

def is_safe(nums):
    inc = all(y > x for x,y in zip(nums, nums[1:]))
    dec = all(y < x for x,y in zip(nums, nums[1:]))
    inrange = all(abs(x - y) <= 3 for x,y in zip(nums, nums[1:]))
    return (inc or dec) and inrange

def remove_one(nums, i):
    return nums[:i] + nums[i+1:]

def brute(nums):
    return any(is_safe(remove_one(nums, x)) for x,_ in enumerate(nums))

print("part1", sum(map(is_safe, numlist)))
print("part2", sum(brute(nums) for nums in numlist))
