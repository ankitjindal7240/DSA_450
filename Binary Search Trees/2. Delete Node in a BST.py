class Node:
    def __init__(self,val):
        self.value=val
        self.left =None
        self.right=None
def inorderSuccesor(root):
    current=root
    while current.left:
        current=current.left
    return current
def deleteNode(root,key):
    if root is None:
        return root
    elif key>root.value:
        root.right=deleteNode(root.right,key)
    elif key<root.value:
        root.left=deleteNode(root.left,key)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        if root.right is None:
            temp=root.left
            root=None
            return temp
        temp=inorderSuccesor(root.right)
        root.value=temp.value
        root.right=deleteNode(root.right,temp.value)

    return root

