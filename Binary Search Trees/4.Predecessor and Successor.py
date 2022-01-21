def findPreSuc(root, key):

    # Base Case
    if root is None:
        return

    # If key is present at root
    if root.key == key:

        # the maximum value in left subtree is predecessor
        if root.left is not None:
            tmp = root.left
            while(tmp.right):
                tmp = tmp.right
            findPreSuc.pre = tmp


        # the minimum value in right subtree is successor
        if root.right is not None:
            tmp = root.right
            while(tmp.left):
                tmp = tmp.left
            findPreSuc.suc = tmp

        return findPreSuc.pre,findPreSuc.suc
