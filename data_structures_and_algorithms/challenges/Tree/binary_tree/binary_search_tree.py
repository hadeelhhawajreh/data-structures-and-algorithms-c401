from binary_tree import *
class binarySearchTree(BinaryTree):
    def add(self,value):
        """
        Add that accepts a value, and adds a new node with that value in the correct location
         in the binary search tree.
        """        
        if not self.root:
            self.root=Node(value)
        else:
            def _walk(node):
                if value<node.value:
                    if not node.left:
                        node.left=Node(value)
                        return
                    else:
                        _walk(node.left)


                else:
                    if not node.right:
                        node.right=Node(value)
                        return

                    else:
                        _walk(node.right)
            _walk(self.root)

    def contains(self, val):

        if not self.root:
            return False
        else:
            def _walk(node):
                if val ==node.value:
                    return True
                elif val< node.value:
                    if self.left :
                        return self.left._walk(val)
                    # return False

                elif val > node.value:
                    if self.right:
                        return self.right._walk(val)
                    # return False
                else:
                    return True
                


if __name__ == "__main__":
    bst=binarySearchTree()
    bst.add(2)
    bst.add(10)
    bst.add(12)
    bst.add(-2)
    bst.add(-1)
    print(bst.contains(5))

        #     2
        #   /    \
        # -2      10
        #   \    /
        #   -1   12

assert bst.root.value==2
assert bst.root.left.value==-2
assert bst.root.left.right.value==-1
assert bst.root.right.value==10
assert bst.root.right.right.value==12
print('Doooooooooooooooooone ,yes')




                    
