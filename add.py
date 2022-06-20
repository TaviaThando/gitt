from os import system

def all_files():
    # if add == "y" or add == "Y" or add == "yes" or add == "Yes" or add == "YES":

        system("git add .")
        print()
        print("FILES ADDED...")
        print()


def single_file():
    fileName = input("What is the name of the file? ")
    system(f"git add {fileName}")


def selected_files():
    
