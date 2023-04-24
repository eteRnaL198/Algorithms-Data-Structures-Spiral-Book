# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/5/ALDS1_5_C

import math
COS60 = math.cos(math.pi/3)
SIN60 = math.sin(math.pi/3)

def print_coordinate(point):
  print(f'{point.x:.8f}', f'{point.y:.8f}')

class Point():
  def __init__(self, x, y):
    self.x = x
    self.y = y

def calc_coordinate(deep, l, r):
  if deep == 0:
    print_coordinate(r)
    return
  
  s = Point((2*l.x + 1*r.x)/3, (2*l.y + 1*r.y)/3)
  t = Point((1*l.x + 2*r.x)/3, (1*l.y + 2*r.y)/3)
  u = Point(((t.x-s.x)*COS60 - (t.y-s.y)*SIN60 + s.x), ((t.x-s.x)*SIN60 + (t.y-s.y)*COS60 + s.y)) # sを中心に回転
  
  calc_coordinate(deep-1, l, s)
  calc_coordinate(deep-1, s, u)
  calc_coordinate(deep-1, u, t)
  calc_coordinate(deep-1, t, r)

deep = int(input())
left = Point(0, 0)
right = Point(100, 0)
print_coordinate(left)
calc_coordinate(deep, left, right)

"""input
1
"""
"""output
0.00000000 0.00000000
33.33333333 0.00000000
50.00000000 28.86751346
66.66666667 0.00000000
100.00000000 0.00000000
"""
