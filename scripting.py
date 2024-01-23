import os
import subprocess


def list_directory(root):
    print("\nThe available directories are: \n")
    subprocess.run(["ls","-a", root])


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
            ask_user = input("\nDo you want to search in another directory??  (Y/N) : ")
            if ask_user.lower() in {"y","yes"}:
                main()
                break
            elif ask_user.lower() in {"n", "no"}:
                print("\nExited Successfully!!!")
                break
            else:
                print("\nInvalid input. Enter again")

    else:
        while True:
            try:
                print(
                    "The virtual environments present in the selected directory are: "
                )
                for index, environments in enumerate(a_virtual, start=1):
                    print(f"{index}.{os.path.basename(environments)}")
                position = int(
                    input(
                        "\nEnter the number of the environment that you want to manage: "
                    )
                )
                if position <= len(a_virtual):
                    index = position - 1
                    manage_virtual(a_virtual[index], a_virtual, index)
                    break

                else:
                    print("\nChoice invalid. Please select again!!!\n")
            except ValueError:
                print("\nEnter a valid integer value\n")


def manage_virtual(dirpath, a_virtual, index):
    print(f"\nYou are inside the virtual environment named {os.path.basename(dirpath)}")
    while True:
        qn = input("\nDo you want to checkout the modules installed? (Y/N): ")

        if qn.lower() in {"y","yes"}:
            print("\n")
            show_dependencies(dirpath)
            break
        elif qn.lower() not in {"n", "no"}:
            print("Invalid input, enter again!!! ")
        else:
            break

    while True:
        ask = input("Do you want to delete the Virtual Environment?? (Y/N): ")
        if ask.lower() in {"y","yes"}:
            del_virtualenv(dirpath)
            del a_virtual[index]
            break
        elif ask.lower() not in {"n", "no"}:
            print("\nInvalid input. Enter again!!! ")
        else:
            break
        
    while True:
        ask_user = input("Exit program or select another virtual environment?? (E/s): ")
        if ask_user.lower() in {"s"}:
            print("\n")
            show_virtual(a_virtual)
        elif ask_user.lower() in {"e","exit"}:
            print("Exited Successfully!!!")
            break
        else:
            print("Invalid input. Enter again!!!\n")


def show_dependencies(item_path):
    bash_command = os.path.join(item_path,"bin/python -m pip list")

    subprocess.run(bash_command, shell=True)
    while True:
        qn = input(
            "\nDo you want to add or delete dependecies? Press S to skip (Add/Del/S): "
        )

        if qn.lower() in {"del","d"}:
            delete_dependency(item_path)
            break
        elif qn.lower() in {"add","a"}:
            add_dependency(item_path)
            break
        elif qn.lower() in {"s"}:
            break
        else:
            print("Invalid input. Enter again!!!")


def delete_dependency(item_path):
    package_name = input("\nEnter the name of the package to be uninstalled: ")
    bash_command = os.path.join(item_path , f"bin/python -m pip uninstall {package_name}")
    subprocess.run(bash_command, shell=True)
    print("\nThe dependency now present in the virtual environment are: ")
    show_dependencies(item_path)


def add_dependency(item_path):
    bash_check = os.path.join(item_path, "bin/python -m pip list")
    result = subprocess.run(bash_check, capture_output=True, text=True, shell=True)
    package_name = input("\n Enter the name of the package to be installed: ")
    if package_name in result.stdout:
        print("\nPackage already installed. Enter another package!!!")
    else:
        bash_command = os.path.join(item_path,f"bin/python -m pip install {package_name}")
        subprocess.run(bash_command, shell=True)
    print("\nThe dependency currently present in the virtual environment are: ")
    show_dependencies(item_path)


def del_virtualenv(item_path):
    bash_command = "rm -rf " + item_path
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
