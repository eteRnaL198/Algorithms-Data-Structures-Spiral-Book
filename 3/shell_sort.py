# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/2/ALDS1_2_D
# 最後に挿入ソートをするまでにだいたい揃えておく
import copy

def insertion_sort(nums, g):
  """
  Args:
    g(int): gap 比較する間隔
  """
  A = copy.copy(nums)
  count = 0
  for i in range(g, len(A)):
    j = i - g
    v = A[i]
    # 今見てる値が最小になるまでズラし続ける
    while j >= 0 and v < A[j]:
      A[j+g] = A[j] 
      j -= g
      count += 1
    A[j+g] = v # 通り過ぎたからgだけ戻る
  return count, A

def shell_sort(nums):
  """
  Args: 
    nums(list[int]): ソートしたい数列
  """
  A = copy.copy(nums)
  gaps = calc_gaps(len(A))
  print(len(gaps))
  print(" ".join(list(map(str, gaps))))
  count = 0
  for g in gaps:
    cnt, A = insertion_sort(A, g)
    count += cnt
  print(str(count))
  return A

def calc_gaps(qty):
  """
  Return:
    gaps(list[int]): 比較する間隔として､g_(n+1)=3*g_n +1の数列を用いると効率が良い
  """
  gaps = [1]
  while qty >= gaps[-1]:
    gaps.append(3*gaps[-1] + 1)
  gaps = gaps[0:-1] # 1つ余計に足してるから最後の要素を除く
  gaps.reverse()
  return gaps

# main
qty = input()
nums = []
for q in range(int(qty)):
  nums.append(int(input()))
sorted_nums = shell_sort(nums)
for n in sorted_nums:
  print(str(n))
