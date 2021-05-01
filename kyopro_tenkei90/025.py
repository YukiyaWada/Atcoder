from collections import deque
N, B = map(int, input().split())

N_digit = len(str(N))

codes = set()
que = deque([(str(i).zfill(len(str(N_digit))), i, 0) for i in range(N_digit)])
while len(que) > 0:
    code, digits_used, n = que.popleft()
    if n < 10:
        que.extend([(code + str(i).zfill(len(str(N_digit))), digits_used + i, n+1) for i in range(N_digit - digits_used + 1)])
    elif digits_used == N_digit:
        codes.add(code)

ans = 0
for code in codes:
    m_num = [int(code[i:i+len(str(N_digit))]) for i in range(0, len(code), len(str(N_digit)))]
    fm = 1
    for i in range(10):
        fm *= i ** m_num[i]
    m = fm + B
    if m <= N:
        for d in str(m):
            m_num[int(d)] -= 1
        if all((m_num[i] == 0 for i in range(10))):
            ans += 1

print(ans)