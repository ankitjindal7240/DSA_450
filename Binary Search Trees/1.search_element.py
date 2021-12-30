class Node:
    def __init__(self,val):
        self.value=val
        self.left =None
        self.right=None

def insertNode(node,key):
    if node is None :
        return Node(key)
    elif node.value==key:
       return node
    elif node.value>key:
        node.left =insertNode(node.left,key)
    elif node.value<key:
        node.right=insertNode(node.right,key)

    return node

def searchNode(node,key):
    if node.value==key or node is None:
       return node
    elif node.value>key:
        return searchNode(node.left,key)
    elif node.value<key:
        return searchNode(node.right,key)


