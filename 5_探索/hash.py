# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/4/ALDS1_4_C

M = 97 # 素数にする
# M = 1046527

def insert(key, value, table):
  i = 0
  while True:
    idx = h(key, i)
    if not table[idx]:
      table[idx] = value
      break
    i += 1

def find(key, value, table):
  i = 0
  while True:
    idx = h(key, i)
    if table[idx] == value:
      print('yes')
      return
    if not table[idx]: # 空に辿り着いた=無かった
      print('no')
      return
    i += 1

def h1(key):
  return key % (M-1)

def h2(key):
  return 1 + (key % (M-2))

def h(key, i):
  return (h1(key) + i*h2(key)) % M

def get_key(arg):
  to_num = { 'A': 1, 'C': 2, 'G': 3, 'T': 4 }
  sum = 0
  for c in arg:
    sum += to_num[c]
  return sum

# main
qty = int(input())
table = [None]*(M+1)
lines = []
for q in range(qty):
  lines.append(input())
for line in lines:
  cmd, arg = line.split(' ')
  key = get_key(arg)
  if cmd == "insert":
    insert(key, arg, table)
    continue
  if cmd == "find":
    find(key, arg, table)
    continue

"""input
6
insert AAA
insert AAC
find AAA
find CCC
insert CCC
find CCC
"""

"""output
yes
no
yes
"""
