def selection_sort(nums):
  count = 0
  for i in range(len(nums)):
    min_j = i
    for j in range(i, len(nums)):
      if nums[min_j] > nums[j]:
        min_j = j
    if min_j != i:
      nums[i], nums[min_j] = nums[min_j], nums[i]
      count += 1
  return nums, count

def print_nums(nums):
  print(" ".join(map(str, nums)))

qty = input()
nums = list(map(int, input().split(' ')))
sorted_nums, count = selection_sort(nums)
print_nums(sorted_nums)
print(count)
