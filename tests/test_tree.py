from data_structures_and_algorithms.challenges.Tree.binary_tree.binary_search_tree  import *
from  data_structures_and_algorithms.challenges.Tree.binary_tree.binary_tree import *
def test_pre():
    Bt=BinaryTree()
    Bt.root=Node(5)
    Bt.root.left=Node(4)
    Bt.root.left.left=Node(2)
    Bt.root.left.right=Node(-1)
    Bt.root.right=Node(14)
    Bt.root.right.left=Node(16)
    Bt.root.right.right=Node(20)
    actual=Bt.PreOrder()
    assert actual==[5, 4, 2, -1, 14, 16, 20]


def test_in():
    Bt=BinaryTree()
    Bt.root=Node(5)
    Bt.root.left=Node(4)
    Bt.root.left.left=Node(2)
    Bt.root.left.right=Node(-1)
    Bt.root.right=Node(14)
    Bt.root.right.left=Node(16)
    Bt.root.right.right=Node(20)
    actual=Bt.InOrder()
    assert actual==[2, 4, -1, 5, 16, 14, 20]



def test_post():
    Bt=BinaryTree()
    Bt.root=Node(5)
    Bt.root.left=Node(4)
    Bt.root.left.left=Node(2)
    Bt.root.left.right=Node(-1)
    Bt.root.right=Node(14)
    Bt.root.right.left=Node(16)
    Bt.root.right.right=Node(20)
    actual=Bt.PostOrder()
    assert actual==[2, -1, 4, 16, 20, 14, 5]


def test_bst():
    bst=binarySearchTree()
    bst.add(2)
    bst.add(10)
    bst.add(12)
    bst.add(-2)
    bst.add(-1)
    assert bst.root.value==2
    assert bst.root.left.value==-2
    assert bst.root.left.right.value==-1
    assert bst.root.right.value==10
    assert bst.root.right.right.value==12


def test_bst_contains_true():
    bst=binarySearchTree()
    bst.add(2)
    bst.add(10)
    bst.add(12)
    bst.add(-2)
    bst.add(-1)
    actual =bst.contains(10)
    assert actual==True



def test_bst_contains_false():
    bst=binarySearchTree()
    bst.add(2)
    bst.add(10)
    bst.add(12)
    bst.add(-2)
    bst.add(-1)
    actual =bst.contains(5)
    assert actual==False


