class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    
class LinkedList:
  def __init__(self):
    self.head = None
    
  def insert_at_beginning(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node
    
  def print_list(self):
    temp = self.head
    while temp:
      print(temp.data, end="-> ")
      temp = temp.next
    print("None")

    
    
llist = LinkedList()
llist.insert_at_beginning(5)
llist.insert_at_beginning(2)
llist.insert_at_beginning(1)

llist.print_list()