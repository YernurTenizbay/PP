import os
import ex2
print('select-a-to rename directory\n','select-b-to print number of files in it\n','select-c-to print number of directories in it\n',
'selsect-d- list content of the directory\n','select-e-to add file to this directory\n','select-f-to add new directory to this directory\n','select-g-to repeat\n')
b=input()
os.path.isfile
os.path.join
basepath = '\\Users\\Ghost Raven\\Desktop\\PP2'
if b=='a':
    os.rename(r':\Users\Ghost Raven\Desktop\PP2\mArat.py',r'file path\NEW file name.file type:\Users\Ghost Raven\Desktop\PP2\Marat.py')
    print("file renamed")
if b=='b':
    
    cnt=0
    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_file():
                cnt=cnt+1
    print(cnt)
elif b=='c':
    files = os.listdir()
    fold= 0
    for x in files:
        if (os.path.isdir(x)):
            fold += 1
    print (fold)
elif b=='d':
    files = os.listdir()
    print (files)
elif b=='e':
    print ("Enter the name of the file:")
    file_name = input()
    open(file_name, "w+").close()
elif b=='f': 
    print ("Enter the name of the directory")
    d_name = input()
    os.mkdir(d_name)
    
elif b=='g':
    ex2.ret()
else:
    open('direct.py')
