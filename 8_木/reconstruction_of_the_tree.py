# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/7/ALDS1_7_D

current_idx = 0
postorder_tree = []


def reconstruct(l, r):  # r:右端idx+1
    if l >= r:
        return
    global current_idx
    i = inorder_tree.index(preorder_tree[current_idx])
    current_val = preorder_tree[current_idx]
    current_idx += 1
    reconstruct(l, i)
    reconstruct(i + 1, r)
    postorder_tree.append(current_val)


if __name__ == "__main__":
    input()  # 接点の数(不要)
    preorder_tree = list(map(int, input().split(" ")))
    inorder_tree = list(map(int, input().split(" ")))
    reconstruct(0, len(preorder_tree))
    print(" ".join(map(str, postorder_tree)))

"""input
5
1 2 3 4 5
3 2 4 1 5
"""
"""output
3 4 2 5 1
"""
