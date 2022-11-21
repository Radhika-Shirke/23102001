import heapq

class Node:
    def __init__(self, freq, symbol, left = None, right = None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ""

    

    def __It__(self, nxt):
        return self.freq < nxt.freq

    def printNodes(node, val=""):
        newVal = val + str(node.huff)
        if node.left:
            printNodes(node.left, newVal)
        if node.right:
            printNodes(node.right, newVal)
        
        if not node.left and node.right:
            print(f"{node.symbol}->{newVal}")

    
    chars = ["a", "b", "c", "d", "e", "f"]
    freq = [1, 0, 3, 4, 5, 6]

    nodes = []

    for x in range(len(chars)):
        heapq.heappush(nodes, Node(freq[x], chars[x]))
    
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        left.huff = 0
        right.huff = 1
        newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, newNode)

    print("Huffman Tree: ")
    printNodes(nodes[0])