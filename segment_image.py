
from graph import Edge, countSortEdge
from disjointSet import Universe
from typing import Tuple
import numpy as np
# from scipy.ndimage.filters import gaussian_filter
from filter import smooth
from sys import exit


def THRESHOLD(size, k):
    '''A macro defined in source cpp
    '''
    return k/ size

# Distance (Difference functions).
def diff(R: np.array, G: np.array, B: np.array, x1: int, y1: int, x2: int, y2: int):
    ''' euclidean pixel distance.
    '''
    return np.sqrt(
        (R[x1,y1].item() - R[x2,y2].item())**2 + (G[x1,y1].item() - G[x2,y2].item())**2 + (B[x1,y1].item() - B[x2,y2].item())**2
        )


# -> Why switch to Manhattan distance?
# If we keep weights as integers we can use counting sort and get better complexity.
def manhattan(R: np.array, G: np.array, B: np.array, x1: int, y1: int, x2: int, y2: int):
    ''' manhattan pixel distance.
    Effect on using various integer conversions on # components beach.jpg
    round -> 1500 
    int (truncation) -> 1100
    ceil -> 1100
    '''
    return int(np.ceil(abs((R[x1,y1].item() - R[x2,y2].item()) + (G[x1,y1].item() - G[x2,y2].item()) + (B[x1,y1].item() - B[x2,y2].item()))))
        

def segment_graph(num_vertices: int, num_edges: int, edges: list, k: float):
    # (4a) Build UnionFind
    U = Universe(num_vertices) # UnionFind(num_vertices)

    # (4b) Initialize thresholds
    thresholds = np.full((num_vertices,1), THRESHOLD(1, k), np.float)

    # DEBUG
    # print(thresholds)
    # exit()

    # for each edge, in non-decreasing weight order...
    for i in range(num_edges):
        pedge = edges[i]
        
        # components conected by this edge
        a = U.find(pedge.a)
        b = U.find(pedge.b)
        #print(f"a:{a}, b: {b}")
        if a != b:
            if (pedge.w <= thresholds[a]) and (pedge.w <= thresholds[b]):
                U.union(a, b)
                a = U.find(a)
                thresholds[a] = pedge.w + THRESHOLD(U.size(a), k)
    
    return U
            
def segment(image: np.array, sigma: float, k: float, minSize: int, dist="manhattan") -> Tuple[np.array, int]:
    ''' This function will take an image along with several arguments and return the
    segmented image.

    one of the outputs: numCss: int
    '''
    # (1) Read each color channel
    # smooth each channel with a guassian filter
    B,G,R = [smooth(i,sigma=sigma) for i in np.dsplit(image,image.shape[-1])]
    w, h, ch = image.shape
    
    # (2) Build edge graph
    # - An important deviation from the code in the original algorithm.  Optionally use manhattan distance instead
    # of euclidean distance.

    edges = []
    num = 0

    if dist == "manhattan":
        for y in range(h):
            for x in range(w):
                print("adding edge:",num,"/",h*w)
                if x < w - 1:   
                    edges.append(Edge(y * w + x, y * w + (x+1), manhattan(R,G,B,x,y,x+1,y)))
                if y < h -1:
                    edges.append(Edge(y * w + x, (y+1) * w + x, manhattan(R,G,B,x,y,x,y+1)))
                if (x < w-1) and (y < h-1):
                    edges.append(Edge(y * w + x, (y+1) * w + (x+1), manhattan(R,G,B,x,y,x+1,y+1)))
                if (x < w-1) and (y > 0):
                    edges.append(Edge(y * w + x, (y-1) * w + (x+1), manhattan(R,G,B,x,y,x+1,y-1)))
                num += 1
        edges = countSortEdge(edges)
        
    else: 
        for y in range(h):
            for x in range(w):
                print("adding edge:",num,"/",h*w)
                if x < w - 1:   
                    edges.append(Edge(y * w + x, y * w + (x+1), diff(R,G,B,x,y,x+1,y)))
                if y < h -1:
                    edges.append(Edge(y * w + x, (y+1) * w + x, diff(R,G,B,x,y,x,y+1)))
                if (x < w-1) and (y < h-1):
                    edges.append(Edge(y * w + x, (y+1) * w + (x+1), diff(R,G,B,x,y,x+1,y+1)))
                if (x < w-1) and (y > 0):
                    edges.append(Edge(y * w + x, (y-1) * w + (x+1), diff(R,G,B,x,y,x+1,y-1)))
                num += 1

        # (3) sort edges -> Python's built-in Timsort
        # in-place sorting.
        # print(len(edges))
        # print(edges[-3])
        # What are these wierd nan values? improper diff function.
        # print([e.w for e in edges if e.w != 0])
        edges.sort()

    # (4) segment graph into a disjoint set
    U: Universe = segment_graph(w*h, len(edges), edges, k)

    # (5) post process small components
    for i in range(num):
        a = U.find(edges[i].a)
        b = U.find(edges[i].b)
        # print(f"a: {U.size(a)}, b: {U.size(b)}, min size: {minSize}")

        if (a != b) and ((U.size(a) < minSize) or (U.size(b) < minSize)):
            
            print("-> applying union")
            U.union(a, b)
    

    numCcs = U.num_sets()
            
    newImg = np.empty(image.shape, image.dtype)

    colordic = {}
    comps = set([])
    # issue: components do not match cpp components.  I get 1 component.  cpp gets 40.
    for y in range(h):
        for x in range(w):
            comp = U.find(y * w + x)

            comps.add(comp)
            if comp not in colordic:
                colordic[comp] = np.random.randint(0,255,3)
            newImg[x, y] = colordic[comp]
    print("segmentation set:",comps)
    return (newImg, numCcs)