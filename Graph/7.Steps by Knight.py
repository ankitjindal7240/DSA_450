import sys
matrix=[]
for i in range(8):
    matrix.append([0]*8)
pos_knight=[]
pos_target=[]
def possible_knight_positions(pos_knight):
    left_up=i
    left_down=i
    right_up=i
    right_down=i

    up_left=i
    up_right=i
    down_left=i
    down_right=i
    return []

def knight_path(pos_knight,pos_target,visited):
    stack=possible_knight_positions(pos_knight)
    mn=sys.maxsize
    while stack:
        next_pos=stack.pop()
        if next_pos==pos_target:
            return mn
        visited=set()
        if next_pos not in visited:
            visited.add(next_pos)
            mn= 1+min( mn,knight_path(pos_knight, pos_target))
            visited.remove(next_pos)

    return sys.maxsize
