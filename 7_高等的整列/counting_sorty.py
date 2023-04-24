# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/6/ALDS1_6_A

# MAX_A = 10000
MAX_A = 100

def create_counts(nums):
  counts = [0] * MAX_A
  for n in nums:
    counts[n] += 1
  return counts

def create_cumulations(nums):
  cumulations = [0] * MAX_A
  sum = 0
  for i in range(len(nums)):
    sum += nums[i]
    cumulations[i] += sum
  return cumulations

def sort(raw_nums, tables):
  sorted_nums = [0] * (len(raw_nums)+1) # idx:1から使う 最後の1個で1だから
  for num in reversed(raw_nums):
    sorted_nums[(tables[num])] = num
    tables[num] -= 1
  return sorted_nums[1:]

# main
qty = input()
nums = list(map(int, input().split(' ')))
counts = create_counts(nums)
cumulations = create_cumulations(counts)
sorted_nums = sort(nums, cumulations)
print(" ".join(map(str, sorted_nums)))

"""input
7
2 5 1 3 2 3 0
"""
"""output
0 1 2 2 3 3 5
"""
