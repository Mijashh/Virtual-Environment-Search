import os

directory= input("Enter directory path to search: ")
os.chdir(directory)
current_directory = os.getcwd()
print(f'Current working directory is now: {current_directory}')
directoryitems=os.listdir(current_directory)
for items in directoryitems:
    print(items)