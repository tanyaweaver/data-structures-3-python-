from source.trees import Node, BTree


def test_cerate_new_node1():
    newNode = Node(3)
    assert newNode.data == 3


def test_cerate_new_node2():
    newNode = Node(3, 2, 1)
    assert newNode.data == 3
    assert newNode.left == 2
    assert newNode.right == 1


def test_create_tress():
    newTree = BTree()
    assert newTree.root is None


def test_insert_node1():
    newTree = BTree()
    newTree.insert_node(5)
    assert newTree.root.data == 5


def test_insert_node2():
    newTree = BTree()
    newTree.insert_node(5)
    newTree.insert_node(2)
    assert newTree.root.left.data == 2


def test_insert_node3():
    newTree = BTree()
    newTree.insert_node(5)
    newTree.insert_node(2)
    assert newTree.root.right is None


def test_insert_node4():
    newTree = BTree()
    newTree.insert_node(5)
    newTree.insert_node(6)
    assert newTree.root.right.data == 6


def test_insert_node5():
    newTree = BTree()
    newTree.insert_node(5)
    newTree.insert_node(6)
    assert newTree.root.left is None


def test_find_empty_tree():
    newTree = BTree()
    assert not newTree.find(5)
