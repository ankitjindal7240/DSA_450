def reverse_str(str):
    if len(str)==0:
        return ""
    return reverse_str(str[1:])+str[0]
print(reverse_str("abcd"))