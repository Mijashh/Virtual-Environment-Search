import os
import subprocess


def listdirectory(dirpath, depth=0):
    a=False
    for item in os.listdir(dirpath):
        
        item_path=os.path.join(dirpath,item)
        
        if os.path.isdir(item_path) and item!=".git":
            print(" "*depth+"-"+item)
            a=searchforenv(item,item_path,depth)
            if a is True:
                break
            listdirectory(item_path,depth+5)

def searchforenv(item,item_path,depth):
    for items in item:
        reqfile=os.path.join(item_path,"pyvenv.cfg")
        if os.path.isfile(reqfile):
            print(" "*depth + f"Virtual environment present in directory {item}!!!")
            qn=input("Do you want to checkout the modules installed? (y/n): ")
            print("\n")
            if qn=="y" or qn=="Y":
                showdependencies(item_path)
            return True

def showdependencies(item_path):
    bash_command=item_path+"/bin/python -m pip list"
    
    subprocess.run(bash_command,shell=True,executable="/bin/zsh")
    qn=input("Do you want to add or delete dependecies?? Press S to skip (Add/Del/S): ")
    if qn=="del" or qn=="Del":
        deletedependency(item_path)
    elif qn=="add" or qn=="Add":
        adddependency(item_path)
    else:
        pass
    print("\n\n")
         
            
def deletedependency(item_path):
    package_name=input("Enter the name of the package to be uninstalled: ")
    bash_command1=item_path+ f"/bin/python -m pip uninstall {package_name}"
    subprocess.run(bash_command1,shell=True, executable="/bin/zsh")
    print("The dependency now present in the virtual environment are: ")
    showdependencies(item_path)
    
def adddependency(item_path):
    package_name=input("\n Enter the name of the package to be installed: ")
    bash_command=item_path+f"/bin/python -m pip install {package_name}"
    subprocess.run(bash_command,shell=True,executable="/bin/zsh")
    print("The dependency now present in the virtual environment are: ")
    showdependencies(item_path)

def main():
    directo= input("Enter directory name to search: ")
    directory=os.path.join("/home/mijashadhikari",directo)
    os.chdir(directory)
    current_directory = os.getcwd()
    listdirectory(current_directory)
    
    
if __name__=="__main__":
    main()
    