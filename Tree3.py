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
    spaces = ' ' * self.get_level() * 4
    prefix = spaces + "|__" if self.parent else ""
    print(prefix + self.data)
    if self.children:
      for child in self.children:
        child.print_tree()
        
  def add_child(self, child):
    child.parent = self
    self.children.append(child)

def build_book_tree():
  root = TreeNode("Library")

  premchand = TreeNode("Premchand")
  premchand.add_child(TreeNode("Godan"))
  premchand.add_child(TreeNode("Gaban"))

  bhagat = TreeNode("Chetan Bhagat")
  bhagat.add_child(TreeNode("Two States"))
  bhagat.add_child(TreeNode("# Idiots"))

  root.add_child(premchand)
  root.add_child(bhagat)

  root.print_tree()
  
if __name__ == '__main__':
  build_book_tree()