#Stanisław Kusiak

import os

def mylistdir(path, depth=0):
    dirlist = os.listdir(path)
    length = len(dirlist)
    for x in dirlist:
        str = x
        for i in range(0, depth):
            str = " " + str
        print(str)
        if os.path.isdir(path+x+"\\"):
            length += mylistdir(path+x+"\\", depth + 1)
    return length

print("\nTotal files: " + str(mylistdir("C:\\Users\\kakao\\source\\repos\\")))
