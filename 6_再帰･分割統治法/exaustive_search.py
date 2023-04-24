# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/5/ALDS1_5_A

def can_make(components, idx, target):
  if target == 0:
    return True
  if idx >= len(components):
    return False
  return can_make(components, idx+1, target) or can_make(components, idx+1, target - components[idx])


#main
qty = input()
components = list(map(int, input().split(' ')))
qty = input()
targets = list(map(int, input().split(' ')))
for t in targets:
  print("yes") if can_make(components, 0, t) else print("no")

"""input
5
1 5 7 10 21
4
2 4 17 8
"""
"""output
no
no
yes
yes
"""
