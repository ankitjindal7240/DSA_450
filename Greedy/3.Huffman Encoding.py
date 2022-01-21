# chars = ['a', 'b', 'c', 'd', 'e', 'f']
# frequency = [ 5, 9, 12, 13, 16, 45]
# nodes=[]
# class Node:
#     def __init__(self,symbol,freq,left=None,right=None):
#         self.symbol=symbol
#         self.freq=freq
#         self.left=left
#         self.right=right
#         self.huff=""
# for i in range(len(chars)):
#     node=Node(chars[i],frequency[i])
#     nodes.append(node)
# while len(nodes)>1:
#     nodes=sorted(nodes, key=lambda x:x.freq)
#     left=nodes[0]
#     right=nodes[1]
#     left.huff=0
#     right.huff=1
#     combined_node=Node(left.symbol+right.symbol,left.freq+right.freq,left,right)
#     nodes.pop(0)
#     nodes.pop(0)
#     nodes.append(combined_node)
#
# def printCodes(node,val):
#     new_val=val +str(node.huff)
#     if node.left:
#         printCodes(node.left,new_val)
#     if node.right:
#         printCodes(node.right,new_val)
#     if (not node.left and not node.right):
#         print(node.symbol , new_val)
# printCodes(nodes[0],"")
# bank = ["011001","000000","010100","001000"]
# bank.pop()
favorite = [3,0,1,4,1]
from _collections import defaultdict
def lasers(favorite):
    employes=len(favorite)
    topo=defaultdict(list)
    for i in range(employes):
        topo[favorite[i]].append(i)
    print(topo)

lasers(favorite)
