class UnionFind():  # 参考: https://note.nkmk.me/python-union-find/
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


H, W = map(int, input().split())
red = [False]*(H*W)
UF = UnionFind(H*W)

Q = int(input())
for _ in range(Q):
    q = input()
    if q[0] == '1':
        _, r, c = map(int, q.split())
        red[(r-1)*W+(c-1)] = True
        for i, j in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if i < 1 or H < i or j < 1 or W < j:
                continue
            if red[(i-1)*W+(j-1)]:
                UF.union((r-1)*W+(c-1), (i-1)*W+(j-1))

    elif q[0] == '2':
        _, ra, ca, rb, cb = map(int, q.split())
        if red[(ra-1)*W+(ca-1)] and red[(rb-1)*W+(cb-1)] and UF.same((ra-1)*W+(ca-1), (rb-1)*W+(cb-1)):
            print('Yes')
        else:
            print('No')