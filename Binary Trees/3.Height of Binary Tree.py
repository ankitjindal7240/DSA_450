ans=0

def heightBT(root,h):
    if root==None:
        return
    global ans
    if h>ans:
        ans=h
    l=root.left
    r=root.right
    if l:
        heightBT(l,h+1)
    if r:
        heightBT(r,h+1)

def heightBT2(root):
    if root==None:
        return -1
    l=heightBT2(root.left)
    r=heightBT2(root.right)
    if l>r:
        return l+1
    else:
        return r+1
