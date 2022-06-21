from os import system

system("git ls-remote > git.txt")

with open('git.txt', 'r') as file:

    while "fatal" in file.read():

        print("""THIS ISN'T A GIT REPO
        TRY:
        echo "# SOEFKWNGFMD" >> README.md
        git init
        git add README.md
        git commit -m "first commit"
        git branch -M main
        git remote add origin git@github.com:TaviaThando/SOEFKWNGFMD.git
        git push -u origin main""")

