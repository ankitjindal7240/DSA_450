class DLLNode:
    def __init__(self,data):
        self.prev=None
        self.next=None
        self.data=data

class DllStack:
    def __init__(self):
        self.head=None
        self.mid=None
        self.count=0
stack=DllStack()
def push(stack,key):
    node=DLLNode(key)
    node.next=stack.head
    stack.count+=1
    if stack.count==1:
        stack.mid=node
    else:
        stack.head.prev=node
        if stack.count %2 !=0:
                stack.mid=stack.mid.prev

    stack.head=node
def pop(stack):
    if stack.count==0:
        print("Stack is empty")
        return -1
    head=stack.head
    element=head.data
    stack.head=head.next
    if stack.head:
        stack.head.prev=None
    stack.count -=1
    if stack.count%2 ==0:
        stack.mid=stack.mid.next
    return element
def middle(stack):
    if stack.count==0:
        return "empty"
    return stack.mid.data


