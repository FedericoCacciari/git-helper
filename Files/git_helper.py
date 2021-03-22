import git                  ##The name of the program is git-helper...
import Files.system_reqs    ##Useful Functions
from pathlib import Path
import os


FoldernotEmpty = object

def clone_repo(repo, dir, Force=False):          ##Clone Repository in directory chosen

    repo_dir = Files.system_reqs.get_repo_name_from_url(repo)
    
    new_dir = dir / repo_dir
    
    try:
    
        if len(list(os.listdir(new_dir))) != 0:
    
            if Force == True:
    
                try:
                    Files.system_reqs.remove_files(dir)
    
                except:
                    git.Git(dir).clone(repo)
    
            elif Force == False:
    
                try:
                    git.Git(dir).clone(repo)
    
                except:
    
                    raise FoldernotEmpty()
    
    except FileNotFoundError:
        
        git.Git(dir).clone(repo)
                

    

def change_branch(dir, branch:str, make=False):
    Repo = git.Repo(dir)

    try:
        Repo.git.switch(branch)
        
    except:
        
        if make == False:
            raise Exception("Branch doesn't exist, use make")
            
        if make == True:
            Repo.git.checkout("-b",branch)
            Repo.git.switch(branch)
            Repo.git.push("--set-upstream", "origin", Repo.head.ref)


def reset_repo(dir, Force=False):
    repository = git.Repo(dir)
    current = repository.active_branch.name
    new = ("origin/"+current)
    if Force == True:
        repository.git.fetch("origin")
        repository.git.reset("--hard", )
    elif Force == False:
        repository.git.pull()