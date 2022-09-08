class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Queue:
  def __init__(self):
    self.head = None
    self.last = None

  def enqueue(self, data) -> None:
    new_node=Node(data)
    if  self.last!= None:
      self.last.next = new_node
    if self.head == None:
      self.head = new_node
    self.last = new_node

  def dequeue(self) -> None:
    if self.head!=None:
      self.head=self.head.next
    if self.head==None:
      self.last=None

  def status(self) -> None:
    elements=''
    current=self.head
    while current!=None:
      elements+=str(current.data)+"=>"
      current=current.next
    print(elements+"None")


# Do not change the following code
queue = Queue()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "enqueue":
    queue.enqueue(int(data[i]))
  elif operations[i] == "dequeue":
    queue.dequeue()
queue.status()
