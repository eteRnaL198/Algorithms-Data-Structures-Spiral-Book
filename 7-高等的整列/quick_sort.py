# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/6/ALDS1_6_C

import copy
import math

# quick sort
def partition(cards, left, right): # right:右端idx+1
  p = left # 基準以下の塊(左側)の末尾idx
  for i in range(left, right):
    if cards[i]["num"] <= cards[right-1]["num"]:
      cards[p], cards[i] = cards[i], cards[p]
      p += 1
  return p-1 # 進め過ぎるから1つ戻す

def quick_sort(cards, left, right):
  p = partition(cards, left, right)
  # print([card["num"] for card in cards], left, p, right)
  if left+1 < p:
    quick_sort(cards, left, p)
  if right-1 > p:
    quick_sort(cards, p+1, right)


# merge sort
def merge(cards, left, mid, right):
  lefts = cards[left:mid]
  rights = cards[mid:right]
  i = 0
  j = 0
  for k in range(left, right):
    if j >= len(rights) or (i < len(lefts) and lefts[i]["num"] <= rights[j]["num"]):
      cards[k] = lefts[i]
      i += 1
      continue
    else:
      cards[k] = rights[j]
      j += 1
      continue

def merge_sort(cards, left, mid, right):
  if left+1 < right:
    merge_sort(cards, left, math.floor((left+mid)/2), mid)
    merge_sort(cards, mid, math.floor((mid+right)/2), right)
    merge(cards, left, mid, right)


def is_equal(cards, cards2):
  flag = True
  for i in range(len(cards)):
    if cards[i]["suit"] != cards2[i]["suit"]:
      flag = False
  return flag

# main
qty = int(input())
cards = []
for i in range(qty):
  suit, card = input().split(' ')
  card = { "suit": suit, "num": int(card) }
  cards.append(card)
cards2 = copy.deepcopy(cards)
quick_sort(cards, 0, qty)
merge_sort(cards2, 0, math.floor(qty/2), qty)
is_stable = is_equal(cards, cards2)
result = 'Stable' if is_stable else 'Not stable'
print(result)
for card in cards:
  print(card['suit'], card['num'])

"""input
6
D 3
H 2
D 1
S 3
D 2
C 1
"""
"""output
Not stable
D 1
C 1
D 2
H 2
D 3
S 3
"""
