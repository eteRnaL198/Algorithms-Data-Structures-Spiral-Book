# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/1/ALDS1_1_A

def insertion_sort(nums: list[int]) -> list[int]:
  for i in range(1, len(nums)):
    v = nums[i]
    j = i - 1
    while j >= 0 and nums[j] > v:
      nums[j+1] = nums[j]
      j -= 1
    nums[j+1] = v # 1つ下げ過ぎちゃうから1つ上げる
    print_nums(nums)
  return nums

def print_nums(nums: list[int]):
  texts = [str(n) for n in nums]
  print(" ".join(texts))

qty = int(input())
line: str = input()
nums: list[int] = [int(n) for n in line.split(' ')]
print_nums(nums)
sorted_nums = insertion_sort(nums)



