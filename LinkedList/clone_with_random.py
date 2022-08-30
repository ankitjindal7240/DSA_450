class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None


class LinkedList:
    def __init__(self, node):
        self.head = node

    # Method to print the list.
    def __repr__(self):
        temp = self.head
        while temp is not None:
            random = temp.random
            random_data = (random.data if
                           random is not None else -1)

            data = temp.data
            print(
                f"Data-{data}, Random data: {random_data}")
            temp = temp.next

        return "\n"

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node


l = LinkedList(Node(5))
l.push(4)
l.push(3)
l.push(2)
l.push(1)

# Setting up random references.
l.head.random = l.head.next.next
l.head.next.random = l.head.next.next.next
l.head.next.next.random = l.head.next.next.next.next
l.head.next.next.next.random = (l.head.next.next.next.next.next)
l.head.next.next.next.next.random = l.head.next
# print(l)
def clone(origional_list):
    #clone the simple part of list
    temp=origional_list.head
    clone_list=LinkedList(Node(temp.data))
    clone_temp=clone_list.head
    temp=temp.next
    while temp:
        clone_temp.next=Node(temp.data)
        clone_temp=clone_temp.next
        temp=temp.next
    # print(clone_list)

    #connect lists
    o=origional_list.head
    ogtemp=o
    o=o.next

    c = clone_list.head
    cltemp=c
    c=c.next

    while o:
        ogtemp.next=cltemp
        cltemp.next=o

        ogtemp = o
        o = o.next
        cltemp = c
        c = c.next
    ogtemp.next = cltemp

    print(origional_list)

    # connect Rnadom pointers
    oghead=origional_list.head
    ogtemp = oghead

    clhead=oghead.next
    cltemp=clhead

    while ogtemp:
        if ogtemp.random:
            cltemp.random =ogtemp.random.next
        ogtemp=ogtemp.next.next
        if ogtemp:
            cltemp=cltemp.next.next
    # print(origional_list)


    #remove old links
    oghead=origional_list.head
    ogtemp = oghead

    clhead=oghead.next
    cltemp=clhead

    while ogtemp:
        ogtemp.next=ogtemp.next.next
        ogtemp=ogtemp.next
        if ogtemp:
            cltemp.next=cltemp.next.next
            cltemp=cltemp.next

    # check
    origional_list=LinkedList(oghead)
    clone_list=LinkedList(clhead)
    print(origional_list)
    print(clone_list)

clone(l)

