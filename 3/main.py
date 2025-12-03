import sys

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

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
print(res)
print(sum(res))


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
