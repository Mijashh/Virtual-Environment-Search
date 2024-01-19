import os


def listdirectory(dirpath):
    for item in os.listdir(dirpath):
        # print(item)
        item_path=os.path.join(dirpath,item)
        
        if os.path.isdir(item_path):
            print(item)
            listdirectory(item_path)
        

directory= input("Enter directory path to search: ")
os.chdir(directory)
current_directory = os.getcwd()
# # print(f'Current working directory is now: {current_directory}')
# directoryitems=os.listdir(current_directory)
# # for items in directoryitems:
# #     print(items)
listdirectory(current_directory)