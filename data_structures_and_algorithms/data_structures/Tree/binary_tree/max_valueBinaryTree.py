from data_structures_and_algorithms.challenges.Tree.binary_tree.binary_search_tree import *
def max_value(self):
    if self.root == None:
        return 'Not found max'
    else:
        max=self.root.value
        left_side=self.max_value(self.root.left)
        right_side=self.max_value(self.root.right)
        if left_side>max:
            max=left_side
        if right_side>max:
            max=right_side
        return max

if __name__ == "__main__":
    Bt=BinaryTree()
    Bt.root=Node(5)
    Bt.root.left=Node(4)
    Bt.root.left.left=Node(2)
    Bt.root.left.right=Node(-1)
    Bt.root.right=Node(14)
    Bt.root.right.left=Node(16)
    Bt.root.right.right=Node(20)
    print(Bt.max_value())