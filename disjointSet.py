class Node:
    def __init__(self, rank: int, p: int, size: int):
        self.rank = rank
        self.p = p
        self.size = size

class Universe:
    '''Disjoint set data structure with the characteristic union & find operations.
    '''
    def __init__(self, n):
        self.elts = []
        self.n = n
        for i in range(n):
            self.elts.append(Node(0,i,1))

    def num_sets(self) -> int: return self.n

    def size(self, x: int) -> int: return self.elts[x].size

    def find(self, x: int) -> int:
        '''The find operation in the unionfind data structure.
        '''
        y = x
        while y != self.elts[y].p:
            y = self.elts[y].p
        self.elts[x].p = y
        return y

    def union(self, x: int, y: int):
        if self.elts[x].rank > self.elts[y].rank:
            self.elts[y].p = x
            self.elts[x].size += self.elts[y].size
        else:
            self.elts[x].p = y
            self.elts[y].size += self.elts[x].size
            if self.elts[x].rank == self.elts[y].rank:
                self.elts[y].rank += 1
        self.n -= 1