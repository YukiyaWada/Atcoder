from collections import deque

N = int(input())
E = [set() for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, input().split())
    E[A].add(B)
    E[B].add(A)

C = [set([1]), set()]
que = deque([(v,1,0) for v in E[1]])
for _ in range(N-1):
    v, p, cp = que.popleft()
    cv = int(bool(cp)^True)
    C[cv].add(v)
    que.extend([(u,v,cv) for u in E[v] if u != p])

print(*(list(C[int(len(C[0]) < len(C[1]))])[:N//2]))