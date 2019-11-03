class Node:
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

    def __str__(self):
        left = 'n/a' if self.left == None else self.left.data
        right = 'n/a' if self.right == None else self.right.data
        return 'N {} L {} R {}'.format(self.data, left, right)

def _traversal(root): 
    # Base Case 
    if root is None: 
        return 0 
    # find max recursive path for left and right node
    l = _traversal(root.left) 
    r = _traversal(root.right) 
    # determine max for left and right child
    max_ = max(l, r)
    # current max including this node
    node_max = max_ + root.data
    _traversal.best = max(_traversal.best, node_max)
    # return current nodes max  
    return node_max 

def findMaxPath(root): 
    # Initialize result 
    _traversal.best = float("-inf")  
    # Compute and return result 
    _traversal(root) 
    return _traversal.best 

t = int(input().strip())
for _ in range(t):
    c = int(input().strip())
    triangle = []
    for _ in range(c):
        n = list(map(int, input().strip().split(' ')))
        triangle.append(n)
    nodes = []
    # initialize nodes
    for i, row in enumerate(triangle):
        node_row = []
        for j, col in enumerate(row):
            node_row.append(Node(col))
        nodes.append(node_row)
    # Build tree of nodes
    for i, row in enumerate(nodes):
        for j, col in enumerate(row):
            try:
                (nodes[i][j]).left = nodes[i+1][j]
                (nodes[i][j]).right = nodes[i+1][j+1]
            except:
                continue
    # Find max Path
    print(findMaxPath(nodes[0][0]))