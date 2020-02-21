import os
def rem():
    open("ex.txt")
    os.remove("ex.txt")
def ren():
    print("dont forget .txt")
    open("ex.txt")
    k=input()
    os.rename("ex.txt",k)  
def add():
    l=open("ex.txt","a")
    l.write(input())
def rew():
    i=open("ex.txt","w")
    i.write(input())
