class TreeNode:
  def __init__(self, data):
    self.data = data
    self.children = []
    self.parent = None
    
  def get_level(self):
    level = 0
    p = self.parent
    while p:
      level += 1
      p = p.parent
      
    return level
  
  def print_tree(self):
    spaces = ' ' * self.get_level() * 5
    prefix = spaces + "|__" if self.parent else ""
    print(prefix + self.data)
    if self.children:
      for child in self.children:
        child.print_tree()
        
  def add_child(self, child):
    child.parent = self
    self.children.append(child) 

def build_Creatures_tree():
  root = TreeNode("Creatures")

  animal = TreeNode("Animals")
  animal.add_child(TreeNode("Lion"))
  animal.add_child(TreeNode("Tiger"))
  animal.add_child(TreeNode("Elephant"))

  bird = TreeNode("Birds")
  bird.add_child(TreeNode("Sparrow"))
  bird.add_child(TreeNode("Peacock"))
  bird.add_child(TreeNode("Peageon"))

  worm = TreeNode("Worms")
  worm.add_child(TreeNode("Snell"))
  worm.add_child(TreeNode("Snack"))

  root.add_child(animal)
  root.add_child(bird)
  root.add_child(worm)

  root.print_tree()
  
if __name__ == '__main__':
  build_Creatures_tree()