str1="abcd"
str2="cdab"

def check_rotation(str1,str2):
    temp=str1+str1
    if temp.count(str2)>0:
        return True
    return False
