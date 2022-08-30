def check(root):
    if root.left==None and root.right==None:
        return True
    if root.left and (root.right==None):
        return False
    if root.right and (root.left==None):
        return False
    if root.right.va>root.left:
        return (check(root.left) and check(root.right))
    else:return False