#!/usr/bin/python3
def uppercase(str):
    newstr = ""
    for i in range(len(str)):
        if (ord(str[i]) >= 97 and ord(str[i]) <= 122):
            j = ord(str[i]) - 32
            newstr += chr(j)
        else:
            newstr += str[i]
    print("{}".format(newstr))
