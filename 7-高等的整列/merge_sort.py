# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/5/ALDS1_5_B

import math

class Nums():
  def __init__(self, data):
    self.data = data
    self.cnt = 0

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
    # print(left, mid, right, lefts, rights)
    for k in range(left, right):
      self.cnt += 1
      if j >= len(rights) or (i < len(lefts) and lefts[i] <= rights[j]):
        self.data[k] = lefts[i]
        i += 1
        continue
      else:
        self.data[k] = rights[j]
        j += 1
        continue
  
  def print_data(self):
    print(" ".join(list(map(str, self.data))))
  
  def print_cnt(self):
    print(self.cnt)

# main
qty = int(input())
nums = Nums(list(map(int, input().split(' '))))
nums.merge_sort(0, math.floor(qty/2), qty)
nums.print_data()
nums.print_cnt()

"""input
10
8 5 9 2 6 3 7 1 10 4
"""
"""output
1 2 3 4 5 6 7 8 9 10
34
"""
