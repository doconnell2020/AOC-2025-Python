import operator
import sys

with open(sys.argv[1], "r") as f:
    lines = f.read().split()

OPS = {"L": operator.sub, "R": operator.add}

res = 0
cur = 50
for line in lines:
    func = OPS[line[0]]
    val = int(line[1:])
    cur = (cur + (func(100, val) % 100)) % 100
    print(f"Line is {line}, OP is {func}, val is {val}")
    if cur == 0:
        res += 1

print(res)
