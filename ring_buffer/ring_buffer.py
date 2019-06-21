class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current == self.capacity:
      self.current = 0
      
    if len(self.storage) <= self.capacity:
      self.storage[self.current] = item
      self.current += 1

  def get(self):
    new_storage = []
    if None in self.storage:
      for item in self.storage:
        if item != None:
          new_storage.append(item)
      return new_storage
    else:
      return self.storage