import os
import subprocess



def list_directory(root):
    print("\nThe available directories are: \n")
    subprocess.run(["ls", root])


def search_for_env(directory):
    virtualenv = []
    reqfile = "pyvenv.cfg"
    for dirpath, dirnames, filenames in os.walk(directory):
        if reqfile in filenames:
            virtualenv.append(dirpath)
    return virtualenv


def show_virtual(a_virtual):
    if len(a_virtual) == 0:
        print("No virtual environments present in selected directory.")
        while True:
            ask_user = input("\nDo you want to search in another directory??  (y/N) : ")
            if ask_user =="y" or ask_user=="Y":
                main()
                break
            elif ask_user in {"n","N"}:
                print("\nExited Successfully!!!")
                break
            else:
                print("\nInvalid input. Enter again")

    else:
        
            while True:
                try:
                    print("The virtual environments present in the selected directory are: ")
                    for index, environments in enumerate(a_virtual, start=1):
                        print(f"{index}.{os.path.basename(environments)}")
                    position = int(
                        input("\nEnter the number of the environment that you want to manage: ")
                    )
                    if position<=len(a_virtual):
                        manage_virtual(a_virtual[position- 1],a_virtual)
                        break
                        
                    else:
                        print("\nChoice invalid. Please select again!!!\n")
                except ValueError:
                    print("\nEnter a valid integer value\n")
                


def manage_virtual(dirpath,a_virtual):
    print(f"\nYou are inside the virtual environment named {os.path.basename(dirpath)}")
    while True:
        qn = input("\nDo you want to checkout the modules installed? (y/N): ")

        if qn == "y" or qn == "Y":
            print("\n")
            show_dependencies(dirpath)
            break
        elif qn not in {"n","N"}: 
            print("Invalid input, enter again!!! ")
        else: 
            break
    
    while True:        
        ask = input("Do you want to delete the Virtual Environment?? (y/N): ")
        if ask == "y" or ask == "Y":
            del_virtualenv(dirpath)
            break
        elif ask not in {"n","N"}:
            print("\nInvalid input. Enter again!!! ")
        else:
            break
    while True:
        ask_user=input("Exit program or select another virtual environment?? (E/s): ")
        if ask_user in {"s", "S"}:
            print("\n")
            show_virtual(a_virtual)
        elif ask_user in {"e","E"}:
            print("Exited Successfully!!!")
            break
        else:
            print("Invalid input. Enter again!!!\n")
            

def show_dependencies(item_path):
    bash_command = item_path+"/bin/python -m pip list"

    subprocess.run(bash_command, shell=True)
    while True:
        qn = input(
        "\nDo you want to add or delete dependecies? Press S to skip (Add/Del/S): "
        )
    
        if qn == "del" or qn == "Del":
            delete_dependency(item_path)
            break
        elif qn == "add" or qn == "Add":
            add_dependency(item_path)
            break
        elif qn in {"s","S"}:
            break
        else:    
            print("Invalid input. Enter again!!!")


def delete_dependency(item_path):
    package_name = input("\nEnter the name of the package to be uninstalled: ")
    bash_command = item_path+f"/bin/python -m pip uninstall {package_name}"
    subprocess.run(bash_command, shell=True)
    print("\nThe dependency now present in the virtual environment are: ")
    show_dependencies(item_path)


def add_dependency(item_path):
    package_name = input("\n Enter the name of the package to be installed: ")
    bash_command = item_path+f"/bin/python -m pip install {package_name}"
    subprocess.run(bash_command, shell=True) #executable=user_shell)
    print("\nThe dependency now present in the virtual environment are: ")
    show_dependencies(item_path)


def del_virtualenv(item_path):
    bash_command = "rm -rf "+item_path
    subprocess.run(bash_command, shell=True)
    print("Environment Deleted Successfully!!! \n")


def main():
    while True:
        root = os.path.expanduser("~")
        list_directory(root)
        directo = input("\nEnter directory name to search for virtual environment: ")
        print("\n")
        directory = os.path.join(root, directo)
        if os.path.isdir(directory):
            a_virtual = search_for_env(directory)
            show_virtual(a_virtual)
            break
        else:
            print("No such directory exists. Enter again")


if __name__ == "__main__":
    main()
