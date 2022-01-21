# detect loop will return  a node in loop
def removeLoop(self,loop_node):
    ptr1=loop_node
    ptr2=loop_node
    k=1
    #count k
    while ptr1.next!=ptr2:
        ptr1=ptr1.next
        k=k+1
    ptr1=self.head
    ptr2=self.head
    # place ptr1 at k distance
    for i in range(k):
        ptr1=ptr1.next

    # let them meet
    while ptr1!=ptr2:
        ptr1=ptr1.next
        ptr2=ptr2.next

    #ptr2 will treverse loop and at end remove loop
    while ptr2.next!=ptr1:
        ptr2=ptr2.next
    ptr2.next=None
