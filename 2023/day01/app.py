from fileinput import input
import re

nums = {k: v for v,k in enumerate("zero|one|two|three|four|five|six|seven|eight|nine".split("|"))}

p2 = r"(\d|"+"|".join(nums.keys())+")"
p3 = r"(\d|"+"|".join(nums.keys())[::-1]+")"

def get_nums(l):
    r = re.findall(p2,l)
    r2 = re.findall(p3,l[::-1])
    nums = [r[0], r2[0][::-1]]
    return int(''.join(map(replace, nums)))

def replace(n):
    return n if n.isdigit() else str(nums[n])
print(sum(map(int, [get_nums(l) for l in input()])))
