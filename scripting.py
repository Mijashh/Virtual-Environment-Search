import os


def listdirectory(dirpath, depth=0):
    for item in os.listdir(dirpath):
        
        item_path=os.path.join(dirpath,item)
        
        if os.path.isdir(item_path):
            print(" "*depth+item)
            listdirectory(item_path,depth+5)

        
            
        

directo= input("Enter directory name to search: ")
directory=os.path.join("/home/mijashadhikari",directo)
os.chdir(directory)
current_directory = os.getcwd()
# # print(f'Current working directory is now: {current_directory}')
# directoryitems=os.listdir(current_directory)
# # for items in directoryitems:
# #     print(items)
listdirectory(current_directory)