# python3
import threading


def compute_height_naive(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)

    return max_height

# this function takes in array nodes that stores the children of all nodes in the tree
# and the root
# and then returns the height of the tree with such root
def tree_height(root, nodes):
    # base case: if the root does not have any children, return height of 1
    if len(nodes[root]) == 0:
        return 1
    # create a variable height and initialize it with 1 to account for the root
    height = 1
    # iterate through the children of the root
    # and recursively calculate the height of the tallest branch starting the root
    for i in range(len(nodes[root])):
        temp = tree_height(nodes[root][i], nodes) + 1
        height = max(height, temp)

    return height


# this function builds an arbitrary tree and returns its height
# eg. n = 5
# parents = 4 -1 4 1 1
# tree is visualized as
#      1
#    /  \
#   3    4
#      /  \
#     0    2
# nodes = [[], [3,4], [], [], [0,2]]
# as shown in array nodes, [0,2] contains child node 0 and 2 of node 4 (4 = index of [0,2] in array nodes)
# height = 3
def compute_height(n, parents):
    # here are n nodes in the tree, so iterate through all nodes and 
    # build an array nodes to store the children of node i with i being the index of array nodes.
    # additionally determine the root of the tree
    nodes = [[] for _ in range(n)]
    root = float("inf")
    for i in range(0, len(parents)):
        if 0 <= parents[i] <= (n-1):
            nodes[parents[i]].append(i)
        if parents[i] == -1:
            root = i

    # unable to determine the root. return height of 0
    if root == float("inf"):
        return 0

    # compute the height of the tree starting from root
    height = tree_height(root, nodes)

    return height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    #n = 10
    #parents = [8, 8, 5, 6, 7, 3, 1, 6, -1, 5]
    assert n == len(parents)
    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
