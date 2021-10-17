
class Edge:
    ''' Connections between nodes in the segment graph.
    node1:  a
    node2:  b
    weight: w
    a --w--> b
    '''
    def __init__(self, a, b, w):
        self.w = w
        self.a = a
        self.b = b

    def __repr__(self):
        return f"{self.a},{self.b},{self.w}"

    # Set up comparisons among edges.
    def __eq__(self, e2):
        if isinstance(e2, Edge):
            return (self.a,self.b,self.w) == (e2.a,e2.b,e2.w) 

    def __lt__(self, e2):
        if isinstance(e2, Edge):
            return self.w < e2.w 

    def __gt__(self, e2):
        if isinstance(e2, Edge):
            return self.w > e2.w

if __name__ == "__main__":
    # Test 1
    e1 = Edge(1,2,10)
    e2 = Edge(3,4,9.5)
    print(e1 > e2)
    