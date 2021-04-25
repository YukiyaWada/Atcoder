from collections import deque

N = int(input())
E = [set() for _ in range(N+1)]
children = [[] for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, input().split())
    E[A].add(B)
    E[B].add(A)

search_que = deque([(1,0)])
calc_que = deque([(1,0)])
ans = 0
while len(search_que) > 0:
    v, p = search_que.popleft()
    search_que.extend([(u, v) for u in E[v] if u != p])
    calc_que.extendleft([(u, v) for u in E[v] if u != p])

while len(calc_que) > 0:
    v, p = calc_que.popleft()
    if len(children[v]) == 0:
        l1 = 1          # l1:最寄りの葉からの最短距離
        l2 = 0          # l2:自らのある2つの子孫を結ぶ最短経路のうち最長の経路の距離
    elif len(children[v]) == 1:
        l1 = children[v][0] + 1
        l2 = 0
    else:
        children[v].sort()
        l1 = children[v][-1] + 1
        l2 = children[v][-1] + children[v][-2] + 1
    
    ans = max(ans, l1, l2)
    children[p].append(l1)

print(ans)