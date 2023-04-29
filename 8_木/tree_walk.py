# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/7/ALDS1_7_C
# 木の巡回


def create_node(p=-1, l=-1, r=-1):
    return {"p": p, "l": l, "r": r}  # parent, left, right


def update_child(tree, key, l=-1, r=-1):
    tree[key]["l"] = l
    tree[key]["r"] = r


def update_parent(tree, key, p):
    tree[key]["p"] = p


def parse_preorder(tree, key):
    print(" " + str(key), end="")
    left = tree[key]["l"]
    if left != -1:
        parse_preorder(tree, left)
    right = tree[key]["r"]
    if right != -1:
        parse_preorder(tree, right)


def parse_inorder(tree, key):
    left = tree[key]["l"]
    if left != -1:
        parse_inorder(tree, left)
    print(" " + str(key), end="")
    right = tree[key]["r"]
    if right != -1:
        parse_inorder(tree, right)


def parse_postorder(tree, key):
    left = tree[key]["l"]
    if left != -1:
        parse_postorder(tree, left)
    right = tree[key]["r"]
    if right != -1:
        parse_postorder(tree, right)
    print(" " + str(key), end="")


# main
qty = int(input())
tree = {}
for _ in range(qty):
    key, left, right = list(map(int, input().split(" ")))
    if not key in tree:  # new node
        tree[key] = create_node(l=left, r=right)
    else:  # existing node
        update_child(tree, key, left, right)
    if left != -1:
        if left in tree:  # existing left child
            update_parent(tree, left, key)
        else:  # new left child
            tree[left] = create_node(p=key)
    if right != -1:
        if right in tree:  # existing right child
            update_parent(tree, right, key)
        else:  # new right child
            tree[right] = create_node(p=key)

root_node = 0
while tree[root_node]["p"] != -1:
    root_node += 1

print("Preorder")
parse_preorder(tree, root_node)
print("\nInorder")
parse_inorder(tree, root_node)
print("\nPostorder")
parse_postorder(tree, root_node)
print()

"""input
9
0 1 4
1 2 3
2 -1 -1
3 -1 -1
4 5 8
5 6 7
6 -1 -1
7 -1 -1
8 -1 -1
"""
"""output
Preorder
 0 1 2 3 4 5 6 7 8
Inorder
 2 1 3 0 6 5 7 4 8
Postorder
 2 3 1 6 7 5 8 4 0
"""
