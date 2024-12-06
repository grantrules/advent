import fileinput

total = 0
rib = 0

for line in fileinput.input():
    x,y,z = [int(n) for n in line.split("x")]

    total += 2*x*y + 2*x*z + 2*y*z + min(x*y,y*z,z*x)
    w,h,_ = sorted([x,y,z])

    rib += w+w+h+h + x*y*z

print(total)
print(rib)
