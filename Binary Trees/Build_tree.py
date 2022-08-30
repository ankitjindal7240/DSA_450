class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

def buildTree():
    data=int(input("Enter data  else enter -1 "))
    if data ==-1:
        return None
    root=Node(data)
    print(f"For left of {data}",end=" ")
    root.left =buildTree()
    print(f"For right of {data}",end=" ")
    root.right =buildTree()
    return root

buildTree()