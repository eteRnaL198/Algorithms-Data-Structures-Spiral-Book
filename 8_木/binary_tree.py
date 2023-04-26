# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/7/ALDS1_7_B
# 二分木


def create_node(p=-1, l=-1, r=-1):
    return {"p": p, "l": l, "r": r}  # parent, left, right


def update_child(nodes, key, l, r):
    nodes[key]["l"] = l
    nodes[key]["r"] = r


def update_parent(nodes, key, p):
    nodes[key]["p"] = p


def get_sibling(nodes, key):
    parent = nodes[key]["p"]
    if parent == -1 or nodes[parent]["l"] == -1 or nodes[parent]["r"] == -1:
        return -1
    left = nodes[parent]["l"]
    if left != key:
        return left
    right = nodes[parent]["r"]
    if right != key:
        return right


def get_degree(nodes, key):
    degree = 0
    if nodes[key]["l"] != -1:
        degree += 1
    if nodes[key]["r"] != -1:
        degree += 1
    return degree


def set_depth(nodes, depths, key, d):
    depths[key] = d
    left = nodes[key]["l"]
    if left != -1:
        set_depth(nodes, depths, left, d + 1)
    right = nodes[key]["r"]
    if right != -1:
        set_depth(nodes, depths, right, d + 1)


def set_height(nodes, heights, key):
    h1 = h2 = 0
    left = nodes[key]["l"]
    if left != -1:
        h1 = set_height(nodes, heights, left) + 1
    right = nodes[key]["r"]
    if right != -1:
        h2 = set_height(nodes, heights, right) + 1
    height = max(h1, h2)
    heights[key] = height
    return height


def set_type(nodes, types, key):
    if nodes[key]["p"] == -1:
        types[key] = "root"
    elif nodes[key]["l"] == -1 and nodes[key]["r"] == -1:
        types[key] = "leaf"
    else:
        types[key] = "internal node"
    left = nodes[key]["l"]
    if left != -1:
        set_type(nodes, types, left)
    right = nodes[key]["r"]
    if right != -1:
        set_type(nodes, types, right)


# main
qty = int(input())
nodes = {}
for _ in range(qty):
    key, l, r = list(map(int, input().split(" ")))
    if not key in nodes:  # new node
        # create itself
        node = create_node(l=l, r=r)
        nodes[key] = node
    else:  # existing node
        update_child(nodes, key, l, r)
    # create it's children
    if l != -1:
        if not l in nodes:
            nodes[l] = create_node(p=key)  # new child
        else:
            update_parent(nodes, l, key)
    if r != -1:
        if not r in nodes:
            nodes[r] = create_node(p=key)  # new child
        else:
            update_parent(nodes, r, key)
root_key = 0
while nodes[root_key]["p"] != -1:
    root_key += 1
types = {}  # key: type
set_type(nodes, types, root_key)
depths = {}  # key: depth
set_depth(nodes, depths, root_key, 0)
heights = {}  # key: height
set_height(nodes, heights, root_key)

for key in sorted(nodes.keys()):
    print(
        "node "
        + str(key)
        + ": parent = "
        + str(nodes[key]["p"])
        + ", sibling = "
        + str(get_sibling(nodes, key))
        + ", degree = "
        + str(get_degree(nodes, key))
        + ", depth = "
        + str(depths[key])
        + ", height = "
        + str(heights[key])
        + ", "
        + str(types[key])
    )

"""input
4
0 1 2
1 3 -1
2 -1 -1
3 -1 -1
"""
"""output
node 0: parent = -1, sibling = -1, degree = 2, depth = 0, height = 2, root
node 1: parent = 0, sibling = 2, degree = 1, depth = 1, height = 1, internal node
node 2: parent = 0, sibling = 1, degree = 0, depth = 1, height = 0, leaf
node 3: parent = -1, sibling = -1, degree = 0, depth = 2, height = 0, root
"""
