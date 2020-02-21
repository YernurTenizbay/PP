import os
import filew as fi
import direct
def ret():
    f=open("ex.txt","w")
    print("write anything")
    f.write(input())
    f.close()
    print(' select-a-to delete file\n','select-b-to rename file\n','select-c-to add content to this file\n',
    'selsect-d- rewrite content of this file\n','select-e-to return to the parent directory\n','select-f-to repeat\n')
    b=input()
    if b=='a':
        fi.rem()
        print("file delited")
        f.close()
    if b=='b':
        fi.ren()
        print("file renamed")
    if b=='c':
        fi.add()
        print("file added")
    if b=='d':
        fi.rew
    if b=='e':
        direct
    if b=='f':
        return(ret())
ret()