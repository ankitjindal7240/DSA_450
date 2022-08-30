stack=[18,19,29,15,16]
import sys
def withSpace(stack):
    suporting=[]
    for i in range(len(stack)):
        if suporting is None:
            suporting.append(stack[i])
        else:
            if suporting[i]>stack[i]:
                suporting.append(stack[i])



def inConstnatSpace(arr):
    stack=[]
    global min
    min=sys.maxsize
    def push(item):
        global min
        if item>min:
            stack.append()
        else:
            ele=2*item-min
            stack.append(ele)
            min=item

    def popup(arr):
        if len(stack)==0:
            return -1
        if stack[-1]<min:
            ans=min
            min= 2*min-stack[-1]
            stack.pop()
        return ans
