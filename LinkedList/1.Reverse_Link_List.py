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
    # l1=LinkList(n1)
    # head=reverseLL(n1)
    # print(head.value,head.next.value)

# words = ["ab","ty","yt","lc","cl","ab"]
# p=0
# pairs=0
# for i in range(len(words)):
#     if words[i]==0:
#         continue
#     if words[i]==words[i][::-1]:
#         p=1
#         words[i]=0
#     else:
#         for j in range(i,len(words)):
#             if words[j] == 0:
#                 continue
#             if words[i] == 0:
#                 continue
#             elif words[j]== words[i][::-1]:
#                 pairs=pairs+1
#                 words[i]=words[j]=0
#
# ans =4*pairs + 2*p

grid = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
stampHeight = 4
stampWidth = 3
for row in grid:
    width = 0
    for i  in range(len(row)):
        if row[i]==1:
            if width==0 or width>=stampWidth:
                width=0
            else:False
        else:
            width=width+1
    if width == 0 or width >= stampWidth:
        width = 0
    else:
        False



for i  in range(len(grid[0])):
    h = 0
    for j  in grid:
        if j[i]==1:
            if h==0 or h>=stampHeight:
                h=0
            else:False
        else:
            h=h+1
    if h == 0 or h >= stampHeight:
        h = 0
    else:
        False





