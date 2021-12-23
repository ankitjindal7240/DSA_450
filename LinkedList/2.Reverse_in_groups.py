class Node:
    def __init__(self,val):
        self.value=val
        self.next=None

class LinkList:
    def __init__(self):
        self.head=None

def reverseLL(head,n):
    if head==None:
        return None
    current=head
    prev=None
    next=None
    i=0
    while head and i<n :
        next=current.next
        current.next=prev
        prev=current
        current=next
        i=i+1
    if current is not None:
        head.next=reverseLL(current,n)
    return prev

# Driver Code
if __name__ == "__main__":
    n1=Node(1)
    n2=Node(2)
    n3=Node(3)
    n4=Node(4)
    n5=Node(5)
    n6=Node(6)
    n7=Node(7)
    n8=Node(8)
    n1.next=n2
    n2.next=n3
    n3.next=n4
    n4.next=n5
    n5.next=n6
    n6.next=n7
    n7.next=n8
    arr=reverseLL(n1,3)
for i in arr:
    print(i.value)