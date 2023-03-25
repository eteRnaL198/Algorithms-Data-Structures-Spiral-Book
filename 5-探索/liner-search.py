# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/4/ALDS1_4_A

def liner_search(targets, num):
  i = 0
  while i < len(targets) and targets[i] != num:
    i += 1
  if i == len(targets):
    return 0
  return 1

# main
qty = int(input())
S = list(map(int, input().split(' ')))
qty = int(input())
T = list(map(int, input().split(' ')))
count = 0
for n in T:
  count += liner_search(S, n)
print(count)

"""input
5
1 2 3 4 5
3
3 4 1
"""
"""output
3
"""
