from collections import deque


class Node(object):
    def __init__(self, val=None, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


def print_tree_nodes_recursively(node):
    print node.val
    if node.left is not None:
        print_tree_nodes_recursively(node.left)
    if node.right is not None:
        print_tree_nodes_recursively(node.right)


def print_tree_nodes_stack(node):
    stack = deque()
    stack.append(node)
    while len(stack) != 0:
        cur = stack.pop()
        if cur is not None:
            print cur.val
            stack.append(cur.right)
            stack.append(cur.left)


def print_tree_nodes_queue(node):
    queue = deque([node])
    while len(queue) != 0:
        cur = queue.popleft()
        if cur is not None:
            print cur.val
            queue.append(cur.left)
            queue.append(cur.right)


if __name__ == '__main__':
    node = Node(10)
    node.left = Node(5)
    node.right = Node(15)
    node.left.left = Node(2)
    node.left.right = Node(7)
    node.right.left = Node(12)
    node.right.right = Node(17)
    # print_tree_nodes_recursively(node)
    # print_tree_nodes_stack(node)
    print_tree_nodes_queue(node)
