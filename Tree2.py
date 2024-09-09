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
    spaces = ' ' * self.get_level() * 10
    prefix = spaces + "|__" if self.parent else ""
    print(prefix + self.data)
    if self.children:
      for child in self.children:
        child.print_tree()
        
  def add_child(self, child):
    child.parent = self
    self.children.append(child) 

def build_product_tree():
  root = TreeNode("Nilupul (CEO)")

  Chinmay = TreeNode("Chinmay (CTO)")
  Chinmay.add_child(TreeNode("Vishwa (Infrastructure Head)"))
  Chinmay.add_child(TreeNode("Dhaval (Cloud Manager)"))
  Chinmay.add_child(TreeNode("Abhijit (App Manager)"))
  Chinmay.add_child(TreeNode("Aamir (Application Head)"))

  Gels = TreeNode("HR Head")
  Gels.add_child(TreeNode("Peter (Recruitment Manager)"))
  Gels.add_child(TreeNode("Waqas (Policy Manager)"))
  
  root.add_child(Chinmay)
  root.add_child(Gels)
  
  root.print_tree()
  
if __name__ == '__main__':
  build_product_tree()