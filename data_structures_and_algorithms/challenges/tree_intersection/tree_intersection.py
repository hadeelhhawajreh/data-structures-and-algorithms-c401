from data_structures_and_algorithms.data_structures.Tree.binary_tree.binary_tree import BinaryTree,Node
def treeIntersection(bt,bt2):
    x=bt.PostOrder()
    y=bt2.PostOrder()
    output=[]
    # for i in range(max(len(bt.PostOrder()),len(bt2.PostOrder()))):
    #     if x[i] in y:
    #         output.append(x[i])
    for i in bt.PostOrder():
        if i in y:
            output.append(i)
    return(output)

if __name__ == "__main__":
    bt=BinaryTree()
    bt.root=Node(25)
    bt.root.left=Node(4)
    bt.root.left.left=Node(2)
    bt.root.left.right=Node(-1)
    bt.root.right=Node(55)
    # bt.root.right.left=Node(60)
    bt.root.right.right=Node(20)
    print(bt.PostOrder())
    bt2=BinaryTree()
    bt2.root=Node(10)
    bt2.root.left=Node(15)
    bt2.root.left.left=Node(20)
    # bt2.root.left.right=Node(25)
    bt2.root.right=Node(55)
    bt2.root.right.left=Node(30)
    bt2.root.right.right=Node(60)
    print(type(bt2.PostOrder()) ,bt2.PostOrder())
    print(max(len(bt.PostOrder()),len(bt2.PostOrder())))
    # x=bt.PostOrder()
    # y=bt2.PostOrder()
    # print(x)
    # print(y)
    # o=[]
    # for i in range(max(len(bt.PostOrder()),len(bt2.PostOrder()))):
    #     if x[i] in y:
    #         o.append(x[i])
    # print(o)
    # [60, 20, 55, 25]
    # [60, 20, 55]
    print(bt.PreOrder())
    print(bt2.PreOrder())
    print( treeIntersection(bt,bt2))