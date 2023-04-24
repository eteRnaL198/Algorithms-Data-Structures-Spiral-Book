# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/5/ALDS1_5_D
# ある数字より左側にあるのに値が大きい数字の個数を求める

import math

class Nums():
  def __init__(self, data):
    self.data = data
    self.inversion_cnt = 0
  
  def merge_sort(self, left, mid, right): # right: 末尾のidx+1
    if left+1 < right:
      self.merge_sort(left, math.floor((left+mid)/2), mid)
      self.merge_sort(mid, math.floor((mid+right)/2), right)
      self.merge(left, mid, right)
  
  def merge(self, left, mid, right):
    lefts = self.data[left:mid]
    rights = self.data[mid:right]
    i = 0
    j = 0
    for k in range(left, right):
      if j >= len(rights) or (i < len(lefts) and lefts[i] <= rights[j]):
        self.data[k] = lefts[i]
        i += 1
        continue
      else:
        self.data[k] = rights[j]
        self.inversion_cnt += len(lefts) - i
        # print(lefts, rights, self.inversion_cnt, len(lefts)-i)
        j += 1
        continue

qty = int(input())
nums = Nums(list(map(int, input().split(' '))))
nums.merge_sort(0, math.floor(len(nums.data)/2), len(nums.data))
print(nums.inversion_cnt)

"""input
5
3 5 2 1 4
"""
"""output
6
"""
