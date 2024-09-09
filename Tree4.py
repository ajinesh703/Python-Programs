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

def build_food_tree():
  root = TreeNode("Food")

  chicken = TreeNode("Chicken Dishes")
  chicken.add_child(TreeNode("Chicken Tikka"))
  chicken.add_child(TreeNode("Chicken Biryani"))
  
  fish = TreeNode("Fish Dishes")
  fish.add_child(TreeNode("Fish Curry"))
  fish.add_child(TreeNode("Fish Fry"))
  
  egg = TreeNode("Egg Dishes")
  egg.add_child(TreeNode("Egg Curry"))
  

  
  root.add_child(chicken)
  root.add_child(fish)
  root.add_child(egg)

  root.print_tree()
  
if __name__ == '__main__':
  build_food_tree()