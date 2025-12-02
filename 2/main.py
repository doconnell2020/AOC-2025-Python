import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().split(",")

ids = []


def part_one(string: str):
    a, b = string.split("-")
    if len(a) == len(b) and len(a) % 2 != 0:
        return
    else:
        even_ns = [str(i) for i in range(int(a), int(b) + 1) if len(str(i)) % 2 == 0]
        valids = [int(n) for n in even_ns if n[: len(n) // 2] == n[len(n) // 2 :]]
        ids.extend(valids)


[part_one(line) for line in lines]

total = sum(ids)
print(f"Part one is : {total}")
