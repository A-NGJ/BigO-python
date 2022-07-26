strings = ['a', 'b', 'c', 'd']
# 4*4 bytes of storage

# push
strings.append('e') # O(1)

# pop
strings.pop() # O(1)

# add first elem
strings.insert(0, 'x') # O(n)

# add to the middle
strings.insert(2, 'alien') # O(n)

class Array:
  def __init__(self):
    self.len = 0
    self.data = {}

  def __str__(self):
    return str(self.__dict__)

  def get(self, index):
    return self.data[index]

  def push(self, item):
    self.data[self.len] = item
    self.len += 1

  def pop(self):
    self.len -= 1
    val = self.data[self.len]
    del self.data[self.len]
    return val

  def delete(self, index):
    delete_item = self.data[index]
    for i in range(index, self.len-1):
      self.data[i] = self.data[i+1]
    del self.data[self.len-1]
    self.len -= 1
    return delete_item

def reverse(s: str) -> str:
  if not isinstance(s, str):
    raise ValueError("input should be a string")
  if len(s) == 1:
    return s
  return s[-1] + reverse(s[:-1])

def merge_sorted(arr1: list, arr2: list) -> list:
  return sorted(arr1 + arr2)

def merge_sorted2(arr1: list, arr2: list) -> list:
  merged = []
  idx1 = idx2 = 0
  while len(merged) is not len(arr1) + len(arr2):
    if idx1 >= len(arr1):
      merged.append(arr2[idx2])
      idx2 += 1
      continue

    if idx2 >= len(arr2):
      merged.append(arr1[idx1])
      idx1 += 1
      continue

    if arr1[idx1] <= arr2[idx2]:
      merged.append(arr1[idx1])
      idx1 += 1
    else:
      merged.append(arr2[idx2])
      idx2 += 1
  return merged