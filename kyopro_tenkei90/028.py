N = int(input())
papers_y = []
papers_x = {}
for i in range(N):
    lx, ly, rx, ry = map(int, input().split())
    papers_y.append((ly, ry))
    if lx in papers_x:
        papers_x[lx].append((i, 'l'))
    else:
        papers_x[lx] = [(i, 'l')]
    if rx in papers_x:
        papers_x[rx].append((i, 'r'))
    else:
        papers_x[rx] = [(i, 'r')]

px = 0
y = [0]*1002
ans = [0]*(N+1)
for x in sorted(list(papers_x.keys())):
    num = 0
    for i in range(len(y)):
        num += y[i]
        if num > 0:
            ans[num] += x - px

    for i, index in papers_x[x]:
        ly, ry = papers_y[i]
        if index == 'l':
            y[ly] += 1
            y[ry] -= 1
        elif index == 'r':
            y[ly] -= 1
            y[ry] += 1
    
    px = x

for a in ans[1:]:
    print(a)