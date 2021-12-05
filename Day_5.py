with open("Input.txt", "r") as fo:
    fileL = []
    for line in fo:
        line = line.rsplit('\n')[0].split(" -> ")
        fileL.append(line)

ansD = {}
ans2D = {}
for line in fileL:   
    f, t = line[0].split(","), line[1].split(",")
    x1, y1, x2, y2 = int(f[0]), int(f[1]), int(t[0]), int(t[1])
    if x1 == x2:
        for i in range(min(y1,y2), max(y1,y2)+1):
            ansD.setdefault((x1, i),0)
            ansD[(x1, i)] += 1
    elif y1 == y2:
        for i in range(min(x1,x2), max(x1,x2)+1):
            ansD.setdefault((i, y1), 0)
            ansD[(i, y1)] += 1
    elif abs(x1-x2) == abs(y1-y2):
        if x1 == y1 and x2 == y2:
            for i in range(min(x1,x2), max(x1,x2)+1):
                ans2D.setdefault((i, i), 0)
                ans2D[(i, i)] += 1
        elif y1 < y2 and x1 > x2 or y1 > y2 and x1 < x2 : # /
            for i in range(abs(y1-y2)+1):
                if x1 > x2:
                    ans2D.setdefault((x1 - i, y1 + i), 0)
                    ans2D[(x1 - i, y1 + i)] += 1
                else:
                    ans2D.setdefault((x1 + i, y1 - i), 0)
                    ans2D[(x1 + i, y1 - i)] += 1
        elif y1 > y2 and x1 > x2 or y1 < y2 and x1 < x2: # \
            for i in range(abs(y1-y2)+1):
                if x1 > x2:
                    ans2D.setdefault((x1 - i, y1 - i), 0)
                    ans2D[(x1 - i, y1 - i)] += 1
                else:
                    ans2D.setdefault((x1 + i, y1 + i), 0)
                    ans2D[(x1 + i, y1 + i)] += 1

part_one = 0
part_two = 0

for coord in ansD.keys():
    if ansD[coord] > 1:
        part_one += 1

for coord in ansD.keys():
    ans2D.setdefault(coord, 0)
    ans2D[coord] += ansD[coord]

for i in ans2D.keys():
    if ans2D[i] > 1:
        part_two += 1

print(part_one)
print(part_two)
