from data_structures_and_algorithms.challenges.tree_intersection.tree_intersection import treeIntersection
from data_structures_and_algorithms.data_structures.Tree.binary_tree.binary_tree import BinaryTree,Node

def test_case1():
    bt=BinaryTree()
    bt.root=Node(25)
    bt.root.left=Node(4)
    bt.root.left.left=Node(2)
    bt.root.left.right=Node(-1)
    bt.root.right=Node(55)
    bt.root.right.left=Node(60)
    bt.root.right.right=Node(20)
    bt2=BinaryTree()
    bt2.root=Node(10)
    bt2.root.left=Node(15)
    bt2.root.left.left=Node(20)
    bt2.root.left.right=Node(25)
    bt2.root.right=Node(55)
    bt2.root.right.left=Node(30)
    bt2.root.right.right=Node(60)
    assert treeIntersection(bt,bt2)==[25, 55, 60, 20]
def test_case2():
    bt3=BinaryTree()
    bt3.root=Node(150)
    bt3.root.left=Node(100)
    bt3.root.left.left=Node(75)
    bt3.root.left.right=Node(160)
    bt3.root.left.right.right=Node(175)
    bt3.root.left.right.left=Node(125)
    bt3.root.right=Node(250)
    bt3.root.right.left=Node(200)
    bt3.root.right.right=Node(350)
    bt3.root.right.right.left=Node(300)
    bt3.root.right.right.right=Node(500)
    bt4=BinaryTree()
    bt4.root=Node(42)
    bt4.root.left=Node(100)
    bt4.root.left.left=Node(15)
    bt4.root.left.right=Node(160)
    bt4.root.left.right.right=Node(175)
    bt4.root.left.right.left=Node(125)
    bt4.root.right=Node(600)
    bt4.root.right.left=Node(200)
    bt4.root.right.right=Node(350)
    bt4.root.right.right.right=Node(4)
    bt4.root.right.right.left=Node(500)
    print(bt3.PreOrder())
    print(bt4.PreOrder())
    print(treeIntersection(bt3,bt4))
    # [125, 175, 160, 100, 200, 500, 350]
    assert treeIntersection(bt3,bt4)==[100,160,125,175,200,350,500]