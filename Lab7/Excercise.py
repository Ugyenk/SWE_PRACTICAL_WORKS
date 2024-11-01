class Node:
    def __init__(self, key):
        """Initialize a node with a key, and left and right children set to None."""
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        """Initialize an empty Binary Search Tree."""
        self.root = None

    def insert(self, key):
        """Inserts a new key into the BST."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        """Helper method to insert a key recursively."""
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def find_max(self):
        """Returns the maximum value in the BST."""
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.val

    def count_nodes(self):
        """Counts and returns the total number of nodes in the BST."""
        return self._count_nodes_recursive(self.root)

    def _count_nodes_recursive(self, node):
        """Helper method to count nodes recursively."""
        if node is None:
            return 0
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)

    def level_order_traversal(self):
        """Performs level-order traversal (breadth-first search) of the BST."""
        levels = []
        if not self.root:
            return levels

        queue = [self.root]
        while queue:
            current_level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(current_level)

        return levels

    def find_height(self):
        """Returns the height of the BST."""
        return self._find_height_recursive(self.root)

    def _find_height_recursive(self, node):
        """Helper method to find height recursively."""
        if node is None:
            return -1  # Height of empty tree is -1
        left_height = self._find_height_recursive(node.left)
        right_height = self._find_height_recursive(node.right)
        return 1 + max(left_height, right_height)

    def is_valid_bst(self):
        """Checks if the tree is a valid Binary Search Tree."""
        return self._is_valid_bst_recursive(self.root, float('-inf'), float('inf'))

    def _is_valid_bst_recursive(self, node, min_val, max_val):
        """Helper method to validate the BST properties recursively."""
        if node is None:
            return True
        if not (min_val < node.val < max_val):
            return False
        return (self._is_valid_bst_recursive(node.left, min_val, node.val) and
                self._is_valid_bst_recursive(node.right, node.val, max_val))

# Example usage of the BST class
bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(18)

print("Maximum value in the BST:", bst.find_max())  # Output: 18
print("Total number of nodes in the BST:", bst.count_nodes())  # Output: 7
print("Level-order traversal of the BST:", bst.level_order_traversal())  # Output: [[10], [5, 15], [3, 7, 12, 18]]
print("Height of the BST:", bst.find_height())  # Output: 2
print("Is the tree a valid BST?", bst.is_valid_bst())  # Output: True
