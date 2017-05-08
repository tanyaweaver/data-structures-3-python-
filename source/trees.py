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

    def _add(self, val, node, inverse):
        if (not inverse and val < node.data) or (inverse and val > node.data):
            if not node.left:
                node.left = Node(val)
            else:
                self._add(val, node.left, inverse)
        else:
            if not node.right:
                node.right = Node(val)
            else:
                self._add(val, node.right, inverse)

    def insert_node(self, val, inverse=False):
        if not self.root:
            self.root = Node(val)
        else:
            self._add(val, self.root, inverse)

    def find(self, val):
        if self.root is None:
            return None
        else:
            return self._find(val, self.root)

    def _find(self, val, node):
        if node is None:
            return None
        elif val == node.data:
            return node
        else:
            if val < node.data:
                return self._find(val, node.left)
            else:
                return self._find(val, node.right)

    def delete_tree(self):
        self.root = None

    def pre_order_traversal(self, node, result=None):
        if node:
            if not result:
                result = []
            result.append(node.data)
            result = self.pre_order_traversal(node.left, result)
            result = self.pre_order_traversal(node.right, result)
        return result

    def in_order_traversal(self, node, result=None):
        if node:
            if not result:
                result = []
            result = self.in_order_traversal(node.left, result)
            result.append(node.data)
            result = self.in_order_traversal(node.right, result)
        return result

    def post_order_traversal(self, node, result=None):
        if node:
            if not result:
                result = []
            result = self.post_order_traversal(node.left, result)
            result = self.post_order_traversal(node.right, result)
            result.append(node.data)
        return result

    def pre_order_traversal_gen(self, node):
        if node:
            yield node.data
            for x in self.pre_order_traversal(node.left):
                yield x
                for x in self.pre_order_traversal(node.right):
                    yield x

    def equal_to_another_tree(self, root1, root2):
        if not root1 and not root2:
            return True
        if (root1 and root2) and (root1.data == root2.data):
            left_subtrees_equal = self.equal_to_another_tree(root1.left, root2.left)
            right_subtrees_equal = self.equal_to_another_tree(root1.right, root2.right)
            return left_subtrees_equal and right_subtrees_equal
        return False

if __name__ == '__main__':
    newTree = BTree()
    newTree.insert_node(5)
    newTree.insert_node(2)
    newTree.insert_node(1)
    newTree.insert_node(3)
    newTree.insert_node(7)
    newTree.insert_node(6)
    newTree.insert_node(8)
    result1 = newTree.pre_order_traversal(newTree.root)
    result2 = newTree.in_order_traversal(newTree.root)
    result3 = newTree.post_order_traversal(newTree.root)
    print result1
    print result2
    print result3
    print list(newTree.pre_order_traversal_gen(newTree.root))
