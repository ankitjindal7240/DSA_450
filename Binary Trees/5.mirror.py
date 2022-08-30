class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.value=val

def mirror(root):
    if root==None:
        return
    curr_node=root
    new_root=Node(curr_node.value)
    if curr_node.left:
        new_root.right=mirror(curr_node.left)
    if curr_node.right:
        new_root.left=mirror(curr_node.right)
    return curr_node
