import sys


# part one
def part_one(lines):
    res = []
    for line in lines:
        a, b = 0, 0
        idx_a = 0
        lst = line[:-1]
        for i in range(len(lst)):
            f = int(lst[i])
            if f > a:
                a = f
                idx_a = i
        lst_2 = line[idx_a + 1 :]
        for j in range(len(lst_2)):
            g = int(lst_2[j])
            if g > b:
                b = g
        res.append(int(str(a) + str(b)))
    return res


def part_two(lines):
    r2 = []
    for line in lines:

        idx = 0
        # b = -12
        num = ""
        while len(num) < 12:
            a = 0
            arr = line[idx:]
            for i in range(len(arr)):
                f = int(arr[i])
                if f > a:
                    a = f
            num += str(a)
            idx +=1
            # b += 1
        r2.append(int(num))
    return r2

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()



    # print(res)
print(f"part one {sum(part_one(lines))}")

print(part_two(lines))
print(f"part two {sum(part_two(lines))}")

#     a, b = 0, 0
#     q = deque(line)
#     try:
#         while q:
#             f = int(q.popleft())
#             if int(f) > a:
#                 a = f
#                 continue
#             g = int(q.pop())
#             if g > b:
#                 b = g
#     except IndexError:
#         pass
#     res.append(int(str(a) + str(b)))
# print(res)
# print(sum(res))
