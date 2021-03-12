import git
from pathlib import Path
from platform import platform
from os import chdir,getenv
from getpass import getuser,getpass

def change_dir(current=True):
    if current is not True:
        if type(current) == str:
            percorso = Path(current)
            chdir(percorso)
        else:
            chdir(current)

##def login(saveit:bool, type=2):


if __name__ == "__main__":
    change_dir("D:\python-project\git\Develop")
    cls()
    print(getenv('username'))