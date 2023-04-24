# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_A
# スタック: Last In First Out (後入れ先出し)

class Stack():
  def __init__(self):
    self.data = [0] # 0番目は使わない [(0), 1, 2, ...]
    self.top = 0
  
  def push(self, x):
    self.data.append(x)
    self.top += 1
  
  def pop(self):
    if self.is_empty:
      raise IndexError("data is empty")
    self.top -= 1
    return self.data.pop(-1)
  
  def is_empty(self):
    return True if self.top == 0 else False

def calculate(formula):
  operators = ["+", "-", "*"]
  stack = Stack()
  for char in formula:
    if not char in operators:
      stack.push(int(char))
      continue
    act = int(stack.pop()) # a+b のb
    pasv = int(stack.pop()) # a+b のa
    if char == "+":
      stack.push(pasv + act)
    elif char == "-":
      stack.push(pasv - act)
    elif char == "*":
      stack.push(pasv * act)
  return stack.pop()

# main
formula = input().split(' ')
solution = calculate(formula)
print(solution)
