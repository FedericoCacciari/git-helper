from logging import raiseExceptions
import git                  ##The name of the program is git-helper...
import Files.system_reqs    ##Useful Functions


def clone_repo(repo, dir, Force=False, returner=False):          ##Clone Repository in directory chosen
    try:                                                         ##Try to clone in directory, if dir not full
        
        git.Git(dir).clone(repo)
        
        if returner == True:
            return(True)
    
    except:                              ##If directory is not empty:
            
        if Force == True:                                        ##Delete file in folder if Forced
            Files.system_reqs.erase_function(dir, repo)
            git.Git(dir).clone(repo)
            
            if returner == True:
                return(True)                                     ##Return True if Returner = True
        
        elif Force == False:
            
            if returner == False:
            
                raise FileExistsError(dir + "Already exists, use Force") ##If returner not True: Error
            
            elif returner == True:                                       ##Else: return False
            
                return(False)

    

def change_branch(dir, branch:str, make=False,returner=False):
    
    Repo = git.Repo(dir)
    
    try:

        Repo.git.switch(branch)
        
        if returner == True:
            return(True)

    except:
        if make == False:
            
            if returner == False:
                raise Exception("Branch doesn't exist, use make")
            
            elif returner == True:
                return(False)
        
        if make == True:
            Repo.git.checkout("-b",branch)
            
            if returner == True:
                return(True)

def pull_repo