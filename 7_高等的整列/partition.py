# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/6/ALDS1_6_B

class Nums():
  def __init__(self, data):
    self.data = data

  def partition(self):
    i = -1
    for j in range(len(self.data)):
      if self.data[j] <= self.data[-1]:
        i += 1
        self.data[i], self.data[j] = self.data[j], self.data[i]
    return i

  def print_data(self, i):
    chars = list(map(str, self.data))
    chars[i] = "[" + chars[i] + "]"
    print(" ".join(chars))

# main
qty = input()
nums = Nums(list(map(int, input().split(' '))))
i = nums.partition()
nums.print_data(i)

"""input
9
3 9 8 1 5 6 2 5
"""
"""output
3 1 5 2 [5] 6 9 8
"""
