class Stack:
  def __init__(self):
    self.list = []

  def isEmpty(self):
    return self.list == []

  def push(self, item):
    self.list.append(item)

  def pop(self):
   return self.list.pop()

  def top(self):
    return self.list[len(self.list) - 1]

  def size(self):
    return len(self.list)

  def pprint(self):
    iNum = 0
    print("[")
    for lis in self.list:
      print(str(iNum) + "\t" + str(lis))
      iNum = iNum + 1
    print("]\n")

  def __str__(self):
    if self.size() == 0:
      return "[ ]"
    sRet = ""
    iNum = 0
    sRet = "[\n"

    for lis in self.list:
      sRet = sRet + str(iNum) + "\t" + str(lis) + "\n"
      iNum = iNum + 1
    sRet = sRet + "]\n"
    return sRet