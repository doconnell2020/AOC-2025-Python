import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().split(",")

ids = []


def length_filter(string: str):
    a, b = string.split("-")
    if len(a) == len(b) and len(a) % 2 != 0:
        return
    else:
        return string


to_check = [length_filter(line) for line in lines]


def foo(string: str):
    a, b = string.split("-")
    even_ns = [str(i) for i in range(int(b[0]), int(b[1]) + 1) if len(str(i)) % 2 == 0]
    print(even_ns)
    valids = [n for n in even_ns if n[: len(n) // 2] == n[len(n) // 2 :]]
    print(valids)


foo("11-22")

# print(lines)
# assert short1 == 1227775554
