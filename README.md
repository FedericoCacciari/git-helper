# Git-Helper - Cli

Git-Helper is an open-source program that allows users to simplify the experience with git.

It is crossplatform, so it should work with all OS, as far as Python, with all the modules, and git are installed.  **It has not been tested with Mac OS yet**.

# Premise - Important:
### This program has been made with the purpose of helping with basics of git.
### There is no guarantee that the program will work and I am not responsible for any damage or deleted file.
# Table Of Conents
- [Git-Helper CLI](#git-helper---cli)
- [Installation](#installation)
- [How to Use](#how-to-use)
    + [Change Directory](#change-directory)
    + [Clone Repository](#clone-repository)
    + [Change Branch](#change-branch)
    + [Update Repository](#update-repository)
    + [Push Repository](#push-repository)
    + [Reset Local Repository](#reset-local-repository)
- [Work in Progress](#work-in-progress)


# Installation
If you are running the program for the first time make sure to have all the requirements installed.

If you want you can directly run "Requirements.py" to automatically install the modules.

The requirements are down here:
- [Python => 3.0](https://www.python.org/)
- [Git](https://git-scm.com/) ***
- [Gitpython (module)](https://github.com/gitpython-developers/GitPython)
- Pathlib (module) **
- OS (module) **
- platform (module) **
- Shutil (module) **
- Stat (module) **
- [Tkinter (module)](https://docs.python.org/3/library/tkinter.html)
- [PySimpleGui (module)](https://pypi.org/project/PySimpleGUI/)

** These module should come preinstalled with Python

*** Make sure you are able run git from every folder, in case you can't [here's how to do it](https://www.answerlookup.com/how-add-git-windows-path-environment-variable)

# How to Use
For now the only way to run the program is by executing "Git HelperCli.py".

The first thing you'll see after the cheange position menu is a menu, where, by typing a number, you select what to do.

## Change Directory
Because now the only way to run the program is by executing it, the script will ask you everytime it opens if you want to change dir.
If you want to stay in the current directory just type "No".

Normally you just enter in the repository directory, but if you want to clone one you have to go one directory up.
## Clone Repository
After you chose where to download the repository it will ask for the link, you can paste both the HTTPS and the SSH link, it will still work.

If a folder with the name of the repository exists and is not empty, the program will ask if you want to continue:

**Pay attention: if you write "Yes" the program will delete all the files in the folder.**

## Change Branch
If you choose to change Branch the script will ask for a name: if the branch doesn't exist will be created.

## Update Repository
If you choose to update the repository the program will download the latest files of the current file, this only if you are not ahead, in that case you'll need to use [Reset-Repository](#reset-local-repository)
## Push Repository
If you want to commit and push your changes you have to select this option. If your changes doesn't match with the current st age the script will if you want to force the changes:

**Pay attention as telling "yes" will overwrite the online branch.**

## Reset Local Repository
Use this function to update your local repository, for matching the online one:

**Pay attention as this will overwrite all the changes made**


# Work in progress

For now there are only the main uses of git, but I'm currently working on the code so that new functions are avaible.

Currently I'm working mainly on these one:

- GUI for the program
- Access and credentials helper
- SSH easy-add (Mainly Windows)
- More code

