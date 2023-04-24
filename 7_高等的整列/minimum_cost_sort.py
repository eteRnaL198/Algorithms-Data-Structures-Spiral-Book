# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/6/ALDS1_6_D
# 最小コストソート

def get_groups(raw_nums, sorted_nums):
  allocated_nums = []
  groups = []
  for i in range(len(raw_nums)):
    num = raw_nums[i]
    if num in allocated_nums:
      continue
    group = []
    while True:
      if num in group:
        break
      group.append(num)
      allocated_nums.append(num)
      num = raw_nums[sorted_nums.index(num)]
    groups.append(group)
  return groups

def calc_min_cost(groups, min_val):
  cost = 0
  for group in groups:
    cost += min(
      sum(group)+(len(group)-2)*min(group),
      sum(group)+min(group)+(len(group)+1)*min_val
    )
  return cost

# main
qty = input()
nums = list(map(int, input().split(' ')))
sorted_nums = sorted(nums)
groups = get_groups(nums, sorted_nums)
print(calc_min_cost(groups, min(nums)))

"""input
7
4 3 2 7 1 6 5
"""
"""output
24
"""
