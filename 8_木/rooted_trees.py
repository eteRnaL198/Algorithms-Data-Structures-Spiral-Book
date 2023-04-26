# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/7/ALDS1_7_A
# 根付き木

class Node():
  def __init__(self, p=-1, n_s=-1, d=-1, h_c=-1):
    self.parent = p
    self.head_child = h_c # 左端の子ども
    self.next_sibling = n_s # 右隣の兄弟
    self.depth = d
    self.type = "" # "root" | "internal node" | "leaf"
  
  def get_children(self, nodes):
    children = []
    id = self.head_child
    while id != -1:
      children.append(id)
      id = nodes[id].next_sibling
    return children

  def set_type(self):
    if self.parent == -1:
      self.type = "root"
      return
    if self.head_child == -1:
      self.type = "leaf"
      return
    self.type = "internal node"

  def is_root(self):
    return True if self.type == "root" else False
  
  def set_depth(self, nodes, id, d):
    if not self.type == "root": raise TypeError("Root node can only call this method.")
    nodes[id].depth = d
    if nodes[id].next_sibling != -1:
      self.set_depth(nodes, nodes[id].next_sibling, d)
    if nodes[id].head_child != -1:
      self.set_depth(nodes, nodes[id].head_child, d+1)

# main
qty = int(input())
nodes = {}
# create nodes
for _ in range(qty):
  id, child_qty, *childs = map(int, input().split(' '))
  head_child = childs[0] if child_qty > 0 else -1
  if not id in nodes.keys():
    nodes[id] = Node(h_c=head_child)
  else:
    nodes[id].head_child = head_child
  for i in range(len(childs)):
    sibling = childs[i+1] if i+1 != len(childs) else -1
    if childs[i] in nodes.keys():
      nodes[childs[i]].parent = id
      nodes[childs[i]].next_sibling = sibling
      continue
    nodes[childs[i]] = Node(p=id, n_s=sibling)

for id in sorted(nodes.keys()):
  nodes[id].set_type()

# find root node
id = 0
while not nodes[id].is_root(): id += 1
root_id = id
nodes[root_id].set_depth(nodes, root_id, 0)

for id in sorted(nodes.keys()):
  print("node {}: parent = {}, depth = {}, ".format(id, nodes[id].parent, nodes[id].depth) + nodes[id].type + ", " + str(nodes[id].get_children(nodes)))
  pass

"""input
13
0 3 1 4 10
1 2 2 3
2 0
3 0
4 3 5 6 7
5 0
6 0
7 2 8 9
8 0
9 0
10 2 11 12
11 0
12 0
"""
"""output
node 0: parent = -1, depth = 0, root, [1, 4, 10]
node 1: parent = 0, depth = 1, internal node, [2, 3]
node 2: parent = 1, depth = 2, leaf, []
node 3: parent = 1, depth = 2, leaf, []
node 4: parent = 0, depth = 1, internal node, [5, 6, 7]
node 5: parent = 4, depth = 2, leaf, []
node 6: parent = 4, depth = 2, leaf, []
node 7: parent = 4, depth = 2, internal node, [8, 9]
node 8: parent = 7, depth = 3, leaf, []
node 9: parent = 7, depth = 3, leaf, []
node 10: parent = 0, depth = 1, internal node, [11, 12]
node 11: parent = 10, depth = 2, leaf, []
node 12: parent = 10, depth = 2, leaf, []
"""
