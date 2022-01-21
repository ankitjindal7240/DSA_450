s = "catsand"
# print(s[:])
dict = {"cats", "cat", "and", "sand", "dog"}

def sentance(s,dict,outp):
    if s in dict:
        print(outp+s)
    for i in range(len(s)):
        if s[:i+1] in dict:
            next_outp=outp+s[:i+1]+" "
            sentance(s[i+1:],dict,next_outp)
sentance(s,dict,"")