import git ##Used for git-option
from pathlib import Path ##Used to be compatible with all systems
import os ##Didn't know if Path could change current working dir
import platform ##Used to find OS to clear shell

whattodo = object
pos = object

def cls(): ##Clear Shell
    name = platform.system()
    if name == "Linux" or name == "Darwin": ##OS = MAC OS or Linux
        os.system("clear")      ##Clear Terminal
    elif name == "Windows":     ##OS = Windows
        os.system("CLS")        ##Clear Terminal

def position_correct(change):       ##Change position if change is different from "no"

    if change == "no":
        current = Path.cwd()
        return(current)

    else:
        os.chdir(Path(change))      ##Change working directory
        return(Path(change))

def clone_repo(repo, dir):          ##Clone Repository in directory chosen
    
    try:
        git.Git(dir).clone(repo)
        print("Directory" + repo + "clone")
    
    except git.exc.GitCommandError:
        raise Exception("Dir exists and is not empty")

def update_repo(repo, dir, element= "All", commit=False):
    git.Repo(repo)

if whattodo == True:
    print("Choose number:\n1. Clone Repo\n2.Update Repo\n ")
    do = input()
    link = input("Insert link:\n")
    clone_repo(link, pos)


if __name__ == "__main__":      ##Trying to make it also as module
    
    print(Path.cwd(), "is current directory")
    
    change = input("Change dir? (dir/no)\n") ##Want to change dir?

    pos = position_correct(change)    ##Check and eventually change dir

    cls()

    print(pos)
    
    whattodo = True