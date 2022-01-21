def minElement(root):
    if root==None:
        return root
    if root.left ==None:
        return root
    return minElement(root.left)