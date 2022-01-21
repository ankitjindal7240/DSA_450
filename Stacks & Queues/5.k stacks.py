class KStack:
    def __init__(self,k,n):
        self.arr=[0]*n
        self.top=[-1]*k
        self.free=0
        self.next=[i+1 for i in range(n)]
        self.next[n-1]=-1

    def isEmpty(self,stackno):
        return self.top[stackno]==-1
    def isFull(self):
        return  self.free==-1
    def push(self,stackno,item):
        if self.isFull():
            return
        insert_at=self.free
        self.arr[insert_at]=item
        self.free=self.next[insert_at]
        self.next[insert_at]=self.top[stackno]
        self.top[stackno]=insert_at

    def pop(self,stackno):
        if self.isEmpty(stackno):
            return None
        item_index=self.top[stackno]
        item=self.arr[item_index]
        self.arr[item_index]=0
        self.top[stackno]=self.next[item_index]
        self.next[item_index]=self.free
        self.free=item_index
        return item

    def printStack(self,stackno):
        top_stack=self.top[stackno]
        while top_stack!=-1:
            print(self.arr[top_stack])
            top_stack=self.next[top_stack]

