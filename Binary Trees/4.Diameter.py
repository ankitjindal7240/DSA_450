max_dia=0
def diameter(root):
    if root.left == None and root.right==None:
        return 0
    global max_dia
    left=0
    right=0
    if root.left:
        left=1+diameter(root.left)
    if root.right:
        right=1+diameter(root.right)

    if (left+right)>max_dia:
        max_dia= left + right
    return max(left,right)

