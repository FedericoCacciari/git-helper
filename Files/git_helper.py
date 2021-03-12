import git                  ##The name of the program is git-helper...
from pathlib import Path    ##Used to be compatible with all systems
import Files.system_reqs    ##Useful Functions


def clone_repo(repo, dir, Force=False, returner=False):          ##Clone Repository in directory chosen
    try:                                                         ##Try to clone in directory, if dir not full
        
        git.Git(dir).clone(repo)
        if returner == True:
            return(True)
    
    except git.exc.GitCommandError:                              ##If directory is not empty:
            
        if Force == True:                                        ##Delete file in folder if Forced

            Files.system_reqs.erase_function(dir, repo)
            git.Git(dir).clone(repo)
            if returner == "True":
                return(True)                                     ##Return True if Returner = True
        
        elif Force == False:
            
            if returner == False:
            
                raise FileExistsError(dir + "Already exists, use Force") ##If returner not True: Error
            
            elif returner == True:                                       ##Else: return False
            
                return(False)

