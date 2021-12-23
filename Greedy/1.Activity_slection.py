start= [1,3,0,5,8,5]
end =  [2,4,6,7,9,9]
n=len(start)


class meeting:

    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos
def maximumMeetings(n,start,end):
    dict={}
    for i in range(n):
        dict[end[i]]=start[i]

    end.sort()
    last_end=0
    activites=0
    for i in range(n):
        if dict[end[i]]>=last_end:
            activites=activites+1
            last_end=end[i]
    return activites
print(maximumMeetings(n,start,end))