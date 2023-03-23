# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_C
# TLE で失敗する

import random

class Memory():
  def __init__(self):
    # self.data = {str(hex(i)): {} for i in range(10**6)} # メモリを擬似的に表現
    self.data = {hex(i): {} for i in range(10)} # メモリを擬似的に表現
  
  def allocate(self, n):
    while True:
      key = random.randint(1, len(self.data.keys())-1)
      if not self.data[hex(key)]:
        break
    self.data[hex(key)] = n
    return hex(key)
  
  def get_address(self, value):
    adrs = self.data[hex(0)]["next"]
    v = None
    while True:
      v = self.data[adrs]["key"]
      if v == value:
        break
      if adrs == hex(0):
        # raise IndexError("key was not found!!")
        return
      adrs = self.data[adrs]["next"]
    return adrs
  
  def free(self, address):
    self.data[address] = {}

  def print(self):
    keys = ""
    adrs = self.data[hex(0)]["next"]
    while True:
      if adrs == hex(0):
        break
      keys += str(self.data[adrs]["key"])+" "
      adrs = self.data[adrs]["next"]
    print(keys.rstrip(' '))
  
class DoubleLinkedList(Memory):
  def __init__(self):
    super().__init__()
    self.sentinel = "0x0"
    self.data[self.sentinel] = {"key": None, "prev": self.sentinel, "next": self.sentinel} # 番兵(先頭を表す特別なノード)
  
  def insert(self, x):
    """連結リストの先頭にキーxを持つ要素を継ぎ足す"""
    node = self.allocate({"key": x, "prev": self.sentinel, "next": self.data[self.sentinel]["next"]})
    self.data[self.data[self.sentinel]["next"]]["prev"] = node # 次の前を新しい要素にする
    self.data[self.sentinel]["next"] = node # 前(番兵)の次を新しい要素にする
  
  def delete(self, x):
    """キーxを持つ最初の要素を連結リストから削除する"""
    address = self.get_address(x)
    if not address:
      return
    self.data[self.data[address]["next"]]["prev"] = self.data[address]["prev"]
    self.data[self.data[address]["prev"]]["next"] = self.data[address]["next"]
    self.free(address)
  
  def deleteFirst(self):
    """連結リストの先頭の要素を削除する"""
    address = self.data[self.sentinel]["next"]
    self.data[self.data[address]["next"]]["prev"] = self.sentinel
    self.data[self.sentinel]["next"] = self.data[address]["next"]
    self.free(address)

  
  def deleteLast(self):
    """連結リストの末尾の要素を削除する"""
    address = self.data[self.sentinel]["prev"]
    self.data[self.data[address]["prev"]]["next"] = self.sentinel
    self.data[self.sentinel]["prev"] = self.data[address]["prev"]
    self.free(address)

class Processor():
  def __init__(self, list):
    self.list = list
  
  def execute(self, cmd, arg=0):
    if cmd == "insert":
      self.list.insert(arg)
      return
    if cmd == "delete":
      self.list.delete(arg)
      return
    if cmd == "deleteFirst":
      self.list.deleteFirst()
      return
    if cmd == "deleteLast":
      self.list.deleteLast()
      return
    raise SyntaxError("Threre are mistakes in the syntax!!")
  
  def print(self):
    self.list.print()
    
# main
qty = int(input())
list = DoubleLinkedList()
processor = Processor(list)
for i in range(qty):
  line = input().split(' ')
  if len(line) == 2: # 引数の有無を確認
    cmd, arg = line
    processor.execute(cmd, int(arg))
  else:
    cmd = line[0]
    processor.execute(cmd)
  # print(processor.list.data) #TODO delete
processor.print()

"""input
8
insert 1000000000
insert 999999999
deleteLast
insert 1234566890
insert 5
deleteFirst
insert 7
delete 5
"""



# test expect: {0: sentinel, 3: {key: 3, p: 0, n: 0} }
# linked_list = DoubleLinkedList()
# linked_list.insert(1)
# linked_list.insert(2)
# linked_list.insert(3)
# linked_list.insert(4)
# linked_list.delete(2)
# linked_list.deleteFirst()
# linked_list.deleteLast()
# print(linked_list.data)
