n=20
arr=[0]*n
k=5

front=[-1]*5
rear=[-1]*5
next=[i+1 for i in range(n)]
next[-1]=-1
global free
free=0

def push(queue_no,elem):
    global free
    if free==-1:
        return "overflow"
    i=free
    free=next[free]
    next[i]=-1
    if front[queue_no]==-1:
        front[queue_no]=i
    arr[i]=elem
    next[rear[queue_no]]=i
    rear[queue_no]=i

def dQueue(queue_no):
    global free

    to_remove=front[queue_no]

    next_front=next[to_remove]

    elem=arr[to_remove]

    arr[to_remove]=0
    next[to_remove]=free
    free=to_remove
    front[queue_no]=next_front

    if front[queue_no]==rear[queue_no]:
        rear[queue_no]=-1


