import copy

def bubble_sort(raw_cards):
  cards = copy.copy(raw_cards)
  for i in range(len(cards)):
    for j in range(len(cards)-1, i, -1):
      if cards[j][1] < cards[j-1][1]: # cards: [H4, C9, ...]
        cards[j], cards[j-1] = cards[j-1], cards[j]
  return cards

def selection_sort(raw_cards):
  """
  Return: list[str]
  """
  cards = copy.copy(raw_cards)
  for i in range(len(cards)):
    min_idx = i
    for j in range(i, len(cards)): # find index of min value
      if cards[min_idx][1] > cards[j][1]: # cards: [H4, C9, ..]
        min_idx = j
    cards[min_idx], cards[i] = cards[i], cards[min_idx]
  return cards

def print_whether_stable(card_b, card):
  """
  Args:
    card_b: str, バブルソートでソートされたカード
    card: str, 比較したいカード
  """
  # バブルソートは安定
  is_stable = True
  for i in range(len(card_b)):
    if card_b[i] != card[i]:
      is_stable = False
  result = "Stable" if is_stable else "Not stable"
  print(result)

def print_cards(cards):
  print(" ".join(cards))

qty = input()
raw_cards = list(input().split(' ')) # [H4, C9, ...]
cards_sorted_by_bubble = bubble_sort(raw_cards)
print_cards(cards_sorted_by_bubble)
print_whether_stable(cards_sorted_by_bubble, cards_sorted_by_bubble)
cards_sorted_by_selection = selection_sort(raw_cards)
print_cards(cards_sorted_by_selection)
print_whether_stable(cards_sorted_by_bubble, cards_sorted_by_selection)
