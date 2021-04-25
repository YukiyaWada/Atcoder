N, K = map(int, input().split())
S = '#' + input()

CS = [None]*(N+1)
CS[0] = {chr(x): 0 for x in range(ord('a'), ord('z')+1)}
for i in range(1, N+1):
    CS[i] = CS[i-1].copy()
    CS[i][S[i]] += 1

i, ans = 0, ''
for k in range(K):
    for x in range(ord('a'), ord('z')+1):
        if CS[-K+k][chr(x)] - CS[i][chr(x)] > 0:
            break
    i += 1
    while S[i] != chr(x):
        i += 1
    ans += chr(x)

print(ans)