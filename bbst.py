class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BBST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return TreeNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        return self._balance(node)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                temp = node.right
                return temp
            elif not node.right:
                temp = node.left
                return temp
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        return self._balance(node)

    def find(self, key):
        return self._find(self.root, key)

    def _find(self, node, key):
        if not node:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self._find(node.left, key)
        else:
            return self._find(node.right, key)

    def _height(self, node):
        if not node:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def _balance(self, node):
        if not node:
            return node

        if self._height(node.left) - self._height(node.right) > 1:
            if self._height(node.left.left) >= self._height(node.left.right):
                node = self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                node = self._rotate_right(node)
        elif self._height(node.right) - self._height(node.left) > 1:
            if self._height(node.right.right) >= self._height(node.right.left):
                node = self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                node = self._rotate_left(node)

        return node

    @staticmethod
    def _rotate_right(node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    @staticmethod
    def _rotate_left(node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root

    @staticmethod
    def _min_value_node(node):
        current = node
        while current.left:
            current = current.left
        return current

