class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self._size = 0

  def append(self, elem):
    if self.head:
      pointer = self.head

      while (pointer.next):
        pointer = pointer.next

      pointer.next = Node(elem)
    else:
      self.head = Node(elem)
    self._size += 1
  
  def __len__(self):
    return self._size
  
  def _getnode(self, index):
    pointer = self.head
    for i in range(index):
      if pointer:
        pointer = pointer.next
      else:
        raise IndexError("list index out of range")
      
    return pointer
      
  def __getitem__(self, index):
    pointer = self._getnode(index)
      
    if pointer:
      return pointer.data
    raise IndexError("list index out of range")

  def __setitem__(self, index, elem):
    pointer = self._getnode(index)
      
    if pointer:
      pointer.data = elem
    else:
      raise IndexError("list index out of range")
    
  def index(self, elem):
    pointer = self.head
    i = 0
    while (pointer):
      if pointer.data == elem:
        return i
      pointer = pointer.next
      i += 1
    
    raise ValueError("{} is not in list".format(elem))
  
  def insert(self, index, elem):
    node = Node(elem)
    if index == 0:
      node.next = self.head
      self.head = node
    else:
      pointer = self._getnode(index - 1)
      node.next = pointer.next
      pointer.next = node
    self._size += 1

  def remove(self, elem):
    if self.head == None:
      raise ValueError("{} is not in list".format(elem))
    elif self.head.data == elem:
      self.head = self.head.next
      self._size -= 1
      return True
    else:
      ancestor = self.head
      pointer = self.head.next
      while (pointer):
        if pointer.data == elem:
          ancestor.next = pointer.next
          pointer.next = None
          return True
        ancestor = pointer
        pointer = pointer.next
      self._size -= 1
    raise ValueError("{} is not in list".format(elem))

  def __contains__(self, item):
    current = self.head
    while current:
      if current.data == item:
        return True
      current = current.next
    return False
  
  def __repr__(self):
    r = ""
    pointer = self.head
    while (pointer):
      r += str(pointer.data) + "->"
      pointer = pointer.next
    return r
  
  def __str__(self):
    return self.__repr__()
