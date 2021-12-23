class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def levelOrder(root):
    queue=[]
    queue.append(root)
    while queue:
        node =queue.pop(0)
        print(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# Driver Code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    levelOrder(root)