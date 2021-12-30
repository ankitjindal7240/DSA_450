def reverseLevel(root):
    queue=[]
    stack=[]
    queue.append(root)
    while queue:
        node =queue.pop(0)
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
        stack.append(node.data)
    print(stack[::-1])

# Driver Code
if __name__ == "__main__":
    class Node:

        # Constructor to create a new node
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
reverseLevel(root)