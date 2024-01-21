import os
import subprocess


def list_directory(dirpath, depth=0):
    if os.path.isdir(dirpath):
        a = False
    for item in os.listdir(dirpath):
        item_path = os.path.join(dirpath, item)

        if os.path.isdir(item_path) and item != ".git":
            print(" " * depth + "-" + item)
            a = search_for_env(item, item_path, depth)
            if a is True:
                continue
            list_directory(item_path, depth + 5)


def search_for_env(item, item_path, depth):
    # for items in item:
    reqfile = os.path.join(item_path, "pyvenv.cfg")
    if os.path.isfile(reqfile):
        print(" " * depth + f"Virtual environment present in directory {item}!!!")
        qn = input("\nDo you want to checkout the modules installed? (y/n): ")
        print("\n")
        if qn == "y" or qn == "Y":
            show_dependencies(item_path)

        ask = input("Do you want to delete the Virtual Environment?? (y/N): ")
        print("\n")
        if ask == "y" or ask == "Y":
            del_virtualenv(item_path)
        return True


def show_dependencies(item_path):
    bash_command = item_path + "/bin/python -m pip list"

    subprocess.run(bash_command, shell=True, executable="/bin/zsh")
    qn = input(
        "\nDo you want to add or delete dependecies? Press S to skip (Add/Del/S): "
    )
    if qn == "del" or qn == "Del":
        delete_dependency(item_path)
    elif qn == "add" or qn == "Add":
        add_dependency(item_path)
    else:
        pass
    print("\n")


def delete_dependency(item_path):
    package_name = input("\nEnter the name of the package to be uninstalled: ")
    bash_command = item_path + f"/bin/python -m pip uninstall {package_name}"
    subprocess.run(bash_command, shell=True, executable="/bin/zsh")
    print("\nThe dependency now present in the virtual environment are: ")
    show_dependencies(item_path)


def add_dependency(item_path):
    package_name = input("\n Enter the name of the package to be installed: ")
    bash_command = item_path + f"/bin/python -m pip install {package_name}"
    subprocess.run(bash_command, shell=True, executable="/bin/zsh")
    print("\nThe dependency now present in the virtual environment are: ")
    show_dependencies(item_path)


def del_virtualenv(item_path):
    bash_command = "rm -rf " + item_path
    subprocess.run(bash_command, shell=True, executable="/bin/zsh")
    print("Environment Deleted Successfully!!! \n")


def main():
    while True:
        root = os.path.expanduser("~")
        print("\nThe available directories are: \n")
        subprocess.run(["ls", root])
        directo = input("\nEnter directory name to search for virtual environment: ")
        print("\n")
        directory = os.path.join(root, directo)
        if os.path.isdir(directory):
            os.chdir(directory)
            current_directory = os.getcwd()
            list_directory(current_directory)
            break
        else:
            print("No such directory exists. Enter again")


if __name__ == "__main__":
    main()
