# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/4/ALDS1_4_B
# 計算量は O(q logn) (q:len(T), n:len(S))

import math

def binary_search(nums, target):
  """
  Args:
    nums(list[int]): 探す先(昇順に並んでいる)
    target(int): この数字がnumsに含まれているか探す
  """
  left_idx = 0 # 左端
  right_idx = len(nums) # 右端(探索対象範囲の値+1)
  while True:
    mid_idx = math.floor((left_idx + right_idx)/2)
    if nums[mid_idx] == target:
      return 1 # 見つかった
    if left_idx == right_idx:
      return 0 # 見つからなかった
    if nums[mid_idx] > target: # 次は左半分から探す
      right_idx = mid_idx
    else: # 次は右半分から探す
      left_idx = mid_idx+1

# main
qty = input()
S = list(map(int, input().split(' ')))
qty = input()
T = list(map(int, input().split(' ')))
count = 0
for t in T:
  count += binary_search(S, t)
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
