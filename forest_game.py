import random

# Node class representing each forest path
class Node:
    def __init__(self, x, y, is_blocked=False):
        self.x = x
        self.y = y
        self.is_blocked = is_blocked  # True if path is blocked (e.g., tree)
        self.right = None  # Pointer to the right node
        self.down = None   # Pointer to the down node

# ForestGrid class representing the 2D linked list (grid of forest paths)
class ForestGrid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.start = self.create_forest(rows, cols)

    # Create a forest grid using linked lists
    def create_forest(self, rows, cols):
        head = Node(0, 0, is_blocked=random.choice([False, False, True]))  # Randomly block some paths
        current_row = head
        
        # Create first row
        current = head
        for col in range(1, cols):
            new_node = Node(0, col, is_blocked=random.choice([False, False, True]))
            current.right = new_node
            current = new_node
        
        # Create remaining rows and link them
        for row in range(1, rows):
            prev_row = current_row
            current_row = Node(row, 0, is_blocked=random.choice([False, False, True]))
            prev_row.down = current_row
            current = current_row
            for col in range(1, cols):
                new_node = Node(row, col, is_blocked=random.choice([False, False, True]))
                current.right = new_node
                prev_row = prev_row.right
                prev_row.down = new_node
                current = new_node
        return head

    # Print the forest grid (visualize the paths)
    def print_forest(self):
        current_row = self.start
        while current_row:
            current = current_row
            while current:
                if current.is_blocked:
                    print(" X ", end="")  # Blocked path
                else:
                    print(" O ", end="")  # Open path
                current = current.right
            print()
            current_row = current_row.down

    # Traverse the grid with player's movement (DFS or BFS based traversal)
    def traverse_forest(self):
        print("\nPlayer starts at (0, 0) and needs to reach ({}, {})".format(self.rows - 1, self.cols - 1))
        stack = [(self.start, [(0, 0)])]  # Stack for DFS with path tracing

        while stack:
            current_node, path = stack.pop()
            x, y = current_node.x, current_node.y

            if x == self.rows - 1 and y == self.cols - 1:
                print("\nCongratulations! You've reached the destination.")
                print("Path taken:", path)
                return

            # Traverse downwards if possible
            if current_node.down and not current_node.down.is_blocked and (current_node.down.x, current_node.down.y) not in path:
                stack.append((current_node.down, path + [(current_node.down.x, current_node.down.y)]))
            
            # Traverse right if possible
            if current_node.right and not current_node.right.is_blocked and (current_node.right.x, current_node.right.y) not in path:
                stack.append((current_node.right, path + [(current_node.right.x, current_node.right.y)]))

        print("\nNo path to the destination was found.")

# Driver Code
if __name__ == "__main__":
    rows = 5  # Number of rows in the forest
    cols = 5  # Number of columns in the forest
    
    # Create the forest grid
    forest = ForestGrid(rows, cols)
    
    # Print the forest structure (grid)
    print("Forest Grid:")
    forest.print_forest()
    
    # Start traversing the forest
    forest.traverse_forest()
