from os import system


def commit():
    commit = input("What would you like your commit message to be? ")
    system(f"git commit -m '{commit}'")