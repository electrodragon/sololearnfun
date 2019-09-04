#!/usr/bin/python

import os

def create_file(filename):
    f = open(filename,'w')
    f.close()

clipfile = '__clipper__.txt'
testfile = '__test__.py'

while True:
    uinp = input("Continue? ([Enter],q,(c)onsole)")
    if uinp.lower() == 'q': break
    if uinp.lower() == 'c':
        os.system('conda activate base && python')
        continue
    os.system("clear")
    create_file(clipfile)
    os.system('adb shell am broadcast -a clipper.get >> '+clipfile)
    # Manipulating ClipBoard Content
    f = open(clipfile,'r')
    cont = f.readlines()
    f.close()
    cont[1] = cont[1][38:]
    cont[-1] = cont[-1][:-2]
    junkcont = []
    for l in cont[8:]:
        if 'Round ' in l:
            break
        junkcont.append(l)
    os.system('rm '+clipfile)
    # Editing Content
    fav_editor = 'nano'
    f = open(testfile, 'w')
    for content in junkcont:
        f.write(content)
    f.close()
    os.system(fav_editor+' '+testfile)
    # generating_Executable_File
    f = open(testfile,'r')
    cont = f.readlines()
    f.close()
    f = open(testfile,'w')
    f.write("#!/home/atta/anaconda3/bin/python\n")
    for content in cont:
        f.write(content)
    f.close()
    os.system('chmod +x '+testfile)
    f = open(testfile,'r')
    cont = f.readlines()[1:]
    f.close()
    print('#######################')
    for l in cont:
        print(l,end='')
    print('#######################')
    os.system('./'+testfile)

        
