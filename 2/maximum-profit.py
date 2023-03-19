# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/1/ALDS1_1_D
# 時刻tにおける価格Rtが与えられ、価格の差Rj-Ri(j>i)の最大値を求める
# e.g. (1行目はデータの数)
  # input
    # 6
    # 5
    # 3
    # 1
    # 3
    # 4
    # 3
  # output
    # 3

max_diff = (-2) * (10**9)
min = 2 * (10**9)

quantity = int(input())
nums: list[int] = []
for q in range(quantity):
  nums.append(int(input()))
for n in nums:
  max_diff = max_diff if max_diff > n - min else n - min
  min = min if min < n else n
print(max_diff)
