N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

m = sum([abs(a-b) for a, b in zip(A, B)])
if K >= m and (K-m) % 2 == 0:
    print('Yes')
else:
    print('No')