N = int(input())
S = input()
MOD = 10**9 + 7

code = {x: i for i, x in enumerate('#atcoder')}
count = [0]*(len('#atcoder'))
count[0] = 1

for s in S:
    if s in 'atcoder':
        i = code[s]
        count[i] = (count[i] + count[i-1]) % MOD
print(count[-1])