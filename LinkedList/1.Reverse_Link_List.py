#Reverse a linked list
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkList:
    def __init__(self):
        self.head=None

def reverseLL(head):

    temp_head=head
    head=head.next
    temp_next_head=head.next
    while head.next:
        head.next=temp_head
        temp_head=head
        head=temp_next_head
        temp_next_head=head.next
    head.next=temp_head
    return head

# Driver Code
if __name__ == "__main__":
    n1=Node(1)
    n2=Node(2)
    n3=Node(3)
    n4=Node(4)
    n5=Node(5)
    n6=Node(6)
    n1.next=n2
    n2.next=n3
    n3.next=n4
    n4.next=n5
    n5.next=n6
    l1=LinkList(n1)
    head=reverseLL(n1)
    print(head.value,head.next.value)
