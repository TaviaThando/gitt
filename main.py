#!/bin/env python
from os import system, path
from add import all_files, selected_files, single_file
from commit import commit

add = input("Would you like to add all your files? (y/n): ")

if add == "y" or add == "Y" or add == "yes" or add == "Yes" or add == "YES":
    all_files()
    commit()


elif add == "n" or add == "N" or add == "no" or add == "No" or add == "NO":

    numOfFiles = input("How many files would you like to add? ")
    print("")

    if numOfFiles == 1:
        single_file()
        commit()

    else:
        for i in range(numOfFiles):
            selected_files()
            commit()

else:
    print("Please give yes or no answers only!!!! (y/Y/yes/Yes/YES/n/N/no/No/NO)!!!!!!!!!!!!!")


pushOrPull = input("Would you like to push or pull your work? ")

if pushOrPull == "push" or pushOrPull == "Push" or pushOrPull == "PUSH":
    system("git push")

elif pushOrPull == "pull" or pushOrPull == "Pull" or pushOrPull == "PULL":
    system("git pull")


