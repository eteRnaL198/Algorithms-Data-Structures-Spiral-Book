# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_B
class Queue():
  def __init__(self):
    self.data = [{}] # 0番目は使わない [{}←head, ?←tail, ...]
    self.head = 0
    self.tail = 1
  
  def enqueue(self, x):
    self.data.append(x)
    self.head = 1
    self.tail += 1
  
  def dequeue(self):
    if self.is_empty():
      raise IndexError("data is empty")
    self.tail -= 1
    if self.tail == 1:
      self.head = 0
    return self.data.pop(1)
  
  def is_empty(self):
    return True if self.head == 0 else False

class Tasks(Queue):
  def __init__(self, qtm):
    self.quantum = qtm
    self.clock = 0
    super().__init__()

  def execute(self):
    while not self.is_empty():
      q = 0
      while True:
        if self.data[self.head]["time"] == 0: # complete task
          self.__print_completed_task()
          self.dequeue()
          break
        if q >= self.quantum: # time is up
          self.postpone()
          break
        self.data[self.head]["time"] -= 1
        q += 1
        self.clock += 1
  
  def __print_completed_task(self):
    name = self.data[self.head]["name"]
    print(name+" "+str(self.clock))
  
  def postpone(self):
    task = self.dequeue()
    self.enqueue(task)

# main
qty, quantum = list(map(int, input().split(' ')))
task = Tasks(quantum) # [{name: foo, time: 100}, {}, ..]
for i in range(qty):
  name, time = input().split(' ')
  task.enqueue({"name": name, "time": int(time)})
task.execute()
