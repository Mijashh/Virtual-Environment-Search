import os
import subprocess


def listdirectory(dirpath, depth=0):
    a=False
    for item in os.listdir(dirpath):
        
        item_path=os.path.join(dirpath,item)
        
        if os.path.isdir(item_path) and item!=".git":
            print(" "*depth+item)
            a=searchforenv(item,item_path,depth)
            if a is True:
                break
            listdirectory(item_path,depth+5)

def searchforenv(item,item_path,depth):
    for items in item:
        reqfile=os.path.join(item_path,"pyvenv.cfg")
        if os.path.isfile(reqfile):
            print(" "*depth + "Virtual environment present!!!")
            dependencies(item_path)
            return True

def dependencies(item_path):
    bash_command=item_path+"/bin/python -m pip list"
    subprocess.run(bash_command,shell=True,executable="/bin/zsh")
         
            
        

if __name__=="__main__":
    directo= input("Enter directory name to search: ")
    directory=os.path.join("/home/mijashadhikari",directo)
    os.chdir(directory)
    current_directory = os.getcwd()
    listdirectory(current_directory)