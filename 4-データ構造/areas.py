# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_D

def calc_area(lines):
  """
  Return:
    area_sum(int): 面積の合計値
    areas(list[{idx, size}, ..]): それぞれの水溜り
  """
  areas = [] # [{idx: 水溜りの左端, size: 値}, ..]
  area_sum = 0
  bc_sla_idxes = [] # \の位置をとっておく
  for i in range(len(lines)):
    if lines[i] == '\\':
      bc_sla_idxes.append(i)
      continue
    if lines[i] == "/" and bc_sla_idxes:
      partial_size = 0
      partial_areas_qty = count_partial_areas_qty(areas, bc_sla_idxes[-1])
      if partial_areas_qty > 0:
        for j in range(partial_areas_qty):
          partial_size += areas.pop()["size"]
      size = i - bc_sla_idxes.pop() + partial_size
      area_sum = area_sum + size - partial_size
      areas.append({"idx": i, "size": size})
      continue
  return [area_sum, areas]

def count_partial_areas_qty(areas, last_idx):
  count = 0
  i = len(areas) - 1 # 後ろから数える
  while True:
    if i < 0:
      break
    if last_idx > areas[i]["idx"]:
      break
    count += 1
    i -= 1
  return count

# main
lines = input()
sum, areas = calc_area(lines)
print(sum)
print((str(len(areas))+" "+" ".join([str(a["size"])  for a in areas])).strip(' '))

"""input
\\//
"""
"""output
4
1 4
"""
