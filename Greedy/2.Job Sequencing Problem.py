class job:
    def __init__(self,id,deadline,profit):
        self.id=id
        self.deadline=deadline
        self.profit =profit
jobs=[]
jobs.append(job('a', 2, 100))
jobs.append(job('b', 1, 19))
jobs.append(job('c', 2, 27))
jobs.append(job('d', 1, 25))
jobs.append(job('e', 3, 15))

jobs=sorted(jobs,key=lambda job:job.deadline)
ans=0
last_profit=jobs[0].profit
last_deadline=jobs[0].deadline
for i in range(1,len(jobs)):
    if jobs[i].deadline==last_deadline:
        if jobs[i].profit>last_profit:
            last_profit=jobs[i].profit
    else:
        ans=ans+last_profit
        last_deadline=jobs[i].deadline
        last_profit=jobs[i].profit
ans=ans+last_profit

print(ans)