# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/4/ALDS1_4_D

import math

W_MAX = 10 # 1つの荷物の最大の重さ
N_MAX = 100 # 荷物の最大の個数

def is_within_capacity(capacity, truck_qty, weights): # その最大積載量とトラックの数で荷物を全て積めるか
  sum = 0
  truck_num = 0
  weight_idx = 0
  while truck_num < truck_qty and weight_idx < len(weights):
    if sum + weights[weight_idx] <= capacity:
      sum += weights[weight_idx]
      weight_idx += 1
      continue
    # 次のトラックを使う
    sum = 0
    truck_num += 1
  return True if weight_idx == len(weights) else False

def find_capacity(truck_qty, weights):
  head = 0
  tail = W_MAX * N_MAX
  while tail - head > 1:
    capacity = math.ceil((head + tail)/2)
    is_within = is_within_capacity(capacity, truck_qty, weights)
    if is_within:
      tail = capacity
    else:
      head = capacity
  return tail
    
# main
cargo_qty, truck_qty = map(int, input().split(" "))
weights = []
for i in range(cargo_qty):
  weights.append(int(input()))
capacity = find_capacity(truck_qty, weights)
print(capacity)

"""input
5 3
8
1
7
3
9
"""
"""output
10
"""
