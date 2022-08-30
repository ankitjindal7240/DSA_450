MAX = 256


def smallestStr(str, n):
    i, j = 0, 0
    chk = [0 for i in range(MAX)]
    for i in range(MAX):
        chk[i] = -1
    for i in range(n):
        if chk[ord(str[i])] == -1:
            chk[ord(str[i])] = i
    for i in range(n):
        flag = False
        for j in range(ord(str[i])):
            if chk[j] > chk[ord(str[i])]:
                flag = True
                break
        if (flag):
            break
    if (i < n):
        ch1 = (str[i])
        ch2 = chr(j)
        for i in range(n):
            if str[i] == ch1:
                str[i] = ch2
            elif str[i] == ch2:
                str[i] = ch1
    return "".join(str)
