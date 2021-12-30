str="aabaa"
def palindrome(str):
    for i in range(len(str)//2):
        if str[i]!=str[-i-1]:
            return "not a palindrime"

    return "palindrome"
print(palindrome(str))