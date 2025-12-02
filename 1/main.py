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
    total = func(cur, val)
    ans = total % 100
    if ans == 0:
        res += 1
    res += abs(total // 100)  # Cant figure part two
    cur = ans


print(res)
