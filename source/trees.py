class Node(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BTree(object):

    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def _add(self, val, node):
        if val < node.data:
            if not node.left:
                node.left = Node(val)
            else:
                self._add(val, node.left)
        else:
            if not node.right:
                node.right = Node(val)
            else:
                self._add(val, node.right)

    def insert_node(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def find(self, val):
        if self.root is None:
            return None
        else:
            return self._find(val, self.root)
