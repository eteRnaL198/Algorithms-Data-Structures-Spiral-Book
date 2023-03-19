# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/2/ALDS1_2_A

def bubble_sort(nums):
  cnt = 0
  should_sort = True
  while should_sort:
    should_sort = False
    for i in range(len(nums)-1, 0, -1):
      if nums[i] < nums[i-1]:
        nums[i], nums[i-1] = nums[i-1], nums[i]
        should_sort = True
        cnt += 1
  print(" ".join([str(n) for n in nums]))
  print(cnt)
  return nums
  
qty = int(input())
nums = list(map(int, input().split(' ')))
bubble_sort(nums)
