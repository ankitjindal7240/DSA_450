s = "thisisagoodday"
# print(s[:])
dict = {"t", "th", "is", "a", "good","day","this"}

def sentance(s,dict,outp):
    if s in dict:
        print(outp+s)
    for i in range(len(s)):
        if s[:i+1] in dict:
            next_outp=outp+s[:i+1]+" "
            sentance(s[i+1:],dict,next_outp)
# sentance(s,dict,"")


s="nitin"
def isPalindrome(s):
    if s==s[::-1]:
        return True
ans=set()
def sentance2(s,outp):
    if isPalindrome(s):
        ans.add(outp+s)
    for i in range(len(s)):
        if isPalindrome(s[:i+1]):
            next_outp=outp+s[:i+1]+" "
            sentance2(s[i+1:],next_outp)
sentance2(s,"")



print(ans)