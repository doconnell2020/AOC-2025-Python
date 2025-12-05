import sys

with open(sys.argv[1]) as f:
    data = f.read()
ins, items = data.split("\n\n")

count = 0

ins = ins.split()
# print(ins)
bounds = [pair.split("-") for pair in ins]
# print(bounds)
items = items.split()
# part one
for i in items:
    i = int(i)
    for pair in bounds:
        a, b = pair
        a = int(a)
        b = int(b)
        if a <= i <= b:
            count += 1
            break
print(f"Count is {count}")

count_2 = 0
stack = [(0, 0)]
# part two
bounds = list(map(lambda x: (int(x[0]), int(x[1])), bounds))
bounds.sort()
print(bounds)
for pair in bounds:
    if stack:
        cur = stack.pop()
        a, b = pair
        a = int(a)
        b = int(b)
        if cur[0] <= a <= cur[1]:
            a = min(a, cur[0])
            b = max(b, cur[1])
            stack.append((a, b))
            continue
        if cur[0] >= b >= cur[1]:
            a = min(a, cur[0])
            b = max(b, cur[1])
            stack.append((a, b))
            continue
        else:
            stack.append(cur)
            a, b = cur
            count_2 += (b - a) + 1
    else:
        stack.append(pair)
        count_2 += (b - a) + 1


# while stack:
#     a, b = stack.pop()
#     count_2 += (b - a) + 1
print(stack)

print(f"Count 2 is {count_2}")
