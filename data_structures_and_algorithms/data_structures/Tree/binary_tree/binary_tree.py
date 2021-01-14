class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    

class BinaryTree:
    """
    Depth First
    Depth first traversal is where we prioritize going through the depth (height) of the tree first. 
    There are multiple ways to carry out depth first traversal,
     and each method changes the order in which we search/print the root.
    Here are three methods for depth first traversal:
    """    
    def __init__(self):
        self.root=None


    def PreOrder(self):
        """
        depth first traversals and returns an array of the values, ordered appropriately.
        Pre-order: root >> left >> right
        """    
        output_pre=[]
        def _walk(node):
            output_pre.append(node.value)
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
        _walk(self.root)
        return output_pre
    
    def InOrder(self):
        """
        depth first traversals and returns an array of the values, ordered appropriately.
        In-order: left >> root >> right
        """        
        output_in=[]
        def _walk(node):
            if node.left:
                _walk(node.left)
            output_in.append(node.value)
            if node.right:
                _walk(node.right)
        _walk(self.root)
        return output_in

    def PostOrder(self):
        """
        depth first traversals and returns an array of the values, ordered appropriately.
        Post-order: left >> right >> root
        """        
        output_post=[]
        def _walk(node):
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
            output_post.append(node.value)
        _walk(self.root)
        return output_post
    
    

if __name__ == "__main__":
    Bt=BinaryTree()
    Bt.root=Node(5)
    Bt.root.left=Node(4)
    Bt.root.left.left=Node(2)
    Bt.root.left.right=Node(-1)
    Bt.root.right=Node(14)
    Bt.root.right.left=Node(16)
    Bt.root.right.right=Node(20)

    print(Bt.PreOrder())
    print('************')
    print(Bt.InOrder())
    print('************')
    print(Bt.PostOrder())


    
    