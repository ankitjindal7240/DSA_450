class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkList:
    def __init__(self):
        self.head=None
def detectLoop(head):
    slow=head
    fast=head
    while slow and fast and fast.next:
        slow=slow.next
        fast= fast.next.next
        if slow==fast:
            return True
    return False