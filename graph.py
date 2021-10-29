from typing import List

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
        self.count = 0
        
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


class CSnode:
    '''An intermediate data structure used by the countingSortEdge algorithm
    '''
    def __init__(self):
        self.count = 0
        self.items = []


def countSortEdge(inputArray: List[Edge]):
    '''A counting sort implmentation that works on Edges.
    '''
    # Find the maximum element in the inputArray
    maxElement= max(inputArray)

    countArrayLength = maxElement.w+1

    # Initialize the countArray with (max+1) zeros
    countArray = [CSnode() for i in range(countArrayLength)]

    # Step 1 -> Traverse the inputArray and increase 
    # the corresponding count for every element by 1
    for el in inputArray: 
        countArray[el.w].count += 1 
        countArray[el.w].items.append(el) 

    #print([i.count for i in countArray])


    # Step 2 -> For each element in the countArray, 
    # sum up its value with the value of the previous 
    # element, and then store that value 
    # as the value of the current element
    for i in range(1, countArrayLength):
        countArray[i].count += countArray[i-1].count 

    # Step 3 -> Calculate element position
    # based on the countArray values
    outputArray = [None for i in range(len(inputArray))]
    i = len(inputArray) - 1
    while i >= 0:
        currentEl = inputArray[i].w
        # print(inputArray[i],inputArray[i].w,countArray[currentEl].count)
        countArray[currentEl].count -= 1
        newPosition = countArray[currentEl].count
        outputArray[newPosition] = inputArray[i]
        i -= 1

    return outputArray

if __name__ == "__main__":
    # Test 1
    e1 = Edge(1,2,10)
    e2 = Edge(3,4,9.5)
    print(e1 > e2)
    