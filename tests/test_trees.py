from source.trees import Node, BTree


def build_tree():
    newTree = BTree()
    vals = [5, 2, 1, 3, 7, 6, 8]
    for val in vals:
        newTree.insert_node(val)
    return newTree


def build_tree_inverse():
    newTree = BTree()
    vals = [5, 2, 1, 3, 7, 6, 8]
    for val in vals:
        newTree.insert_node(val, inverse=True)
    return newTree


def build_tree2():
    newTree = BTree()
    vals = [5, 2, 1, 4, 17, 6]
    for val in vals:
        newTree.insert_node(val)
    return newTree


def build_tree3():
    newTree = BTree()
    vals = [7, 6, 8]
    for val in vals:
        newTree.insert_node(val)
    return newTree


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


def test_find_existing_node1():
    newTree = build_tree()
    assert newTree.find(5).data == 5


def test_find_existing_node2():
    newTree = build_tree()
    assert newTree.find(6).data == 6


def test_find_existing_node3():
    newTree = build_tree()
    assert newTree.find(2).data == 2


def test_delete_tree():
    newTree = build_tree()
    newTree.delete_tree()
    assert newTree.root is None


def test_find_non_existing_node():
    newTree = build_tree()
    assert not newTree.find(17)


def test_pre_order_traversal():
    newTree = build_tree()
    assert newTree.pre_order_traversal(newTree.root) == [5, 2, 1, 3, 7, 6, 8]


def test_in_order_traversal():
    newTree = build_tree()
    assert newTree.in_order_traversal(newTree.root) == [1, 2, 3, 5, 6, 7, 8]


def test_in_order_traversal_inverse_tree():
    newTree = build_tree_inverse()
    assert newTree.in_order_traversal(newTree.root) == [8, 7, 6, 5, 3, 2, 1]


def test_post_order_traversal():
    newTree = build_tree()
    assert newTree.post_order_traversal(newTree.root) == [1, 3, 2, 6, 8, 7, 5]


def test_equal_to_another_tree1():
    tree1 = build_tree()
    tree2 = build_tree()
    assert tree1.equal_to_another_tree(tree1.root, tree2.root) is True


def test_equal_to_another_tree2():
    tree1 = build_tree()
    tree2 = build_tree_inverse()
    assert tree1.equal_to_another_tree(tree1.root, tree2.root) is False


def test_equal_to_another_tree3():
    tree1 = build_tree()
    tree2 = BTree()
    assert tree1.equal_to_another_tree(tree1.root, tree2.root) is False


def test_equal_to_another_tree4():
    tree2 = build_tree()
    tree1 = BTree()
    assert tree1.equal_to_another_tree(tree1.root, tree2.root) is False


def test_equal_to_another_tree5():
    tree1 = build_tree()
    tree2 = build_tree2()
    assert tree1.equal_to_another_tree(tree1.root, tree2.root) is False


def test_is_subtree_of_another_tree1():
    tree1 = build_tree()
    tree2 = build_tree3()
    assert tree2.is_subtree_of_another_tree(tree1) is True


def test_is_subtree_of_another_tree2():
    tree1 = build_tree()
    assert tree1.is_subtree_of_another_tree(tree1) is True


def test_is_subtree_of_another_tree3():
    tree1 = build_tree()
    tree2 = build_tree3()
    assert tree1.is_subtree_of_another_tree(tree2) is False


def test_is_subtree_of_another_tree4():
    tree1 = build_tree()
    tree2 = BTree()
    assert tree1.is_subtree_of_another_tree(tree2) is False


def test_is_subtree_of_another_tree5():
    tree1 = build_tree()
    tree2 = BTree()
    assert tree2.is_subtree_of_another_tree(tree1) is False
