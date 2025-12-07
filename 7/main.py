import sys

with open(sys.argv[1]) as f:
    data = f.read()

data = data.splitlines()
data = [list(d) for d in data]
print(data)
# part one
n_splits = 0
for i, line in enumerate(data):
    if "S" in line:
        continue
    else:
        for j, space in enumerate(line):
            if data[i - 1][j] == "S":
                data[i][j] = "|"
            elif space == "^" and data[i - 1][j] == "|":
                data[i][j - 1] = "|"
                data[i][j + 1] = "|"
                n_splits += 1
            elif data[i - 1][j] == "|":
                data[i][j] = "|"
            else:
                continue
    # print(line)
print(n_splits)

# part two: possible paths, thanks reddit for hints
with open(sys.argv[1]) as f:
    data = f.read()

data = data.splitlines()
data = [list(d) for d in data]
for i, line in enumerate(data):
    if "S" in line:
        continue
    else:
        for j, space in enumerate(line):
            abv = data[i - 1][j]
            if abv == "S":
                data[i][j] = 1
            elif space == "^" and isinstance(abv, int):
                left = data[i][j - 1]
                if isinstance(left, int):
                    data[i][j - 1] += abv
                else:
                    data[i][j - 1] = abv

                right = data[i][j + 1]
                if isinstance(right, int):
                    data[i][j + 1] += abv
                else:
                    data[i][j + 1] = abv
            elif isinstance(abv, int):
                data[i][j] = abv
            else:
                continue
        print(line)
total = sum([d for d in line if isinstance(d, int)])
print(total)
