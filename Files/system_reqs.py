from pathlib import Path                ##Manage directory in all OS.
import os                               ##Didn't know if Path could change current working dir
import platform                         ##Used to find OS to clear shell
import shutil
import stat

def cls():                              ##Clear Shell
    
    name = platform.system()
    
    if name == "Linux" or name == "Darwin": ##OS = MAC OS or Linux
    
        os.system("clear")              ##Clear Terminal
    
    elif name == "Windows":             ##OS = Windows
    
        os.system("CLS")                ##Clear Terminal

def position_correct(change):           ##Change position if change is different from "no"
    
    no_list = ["no", "No","nO", "NO", "False", "false", "FALSE"]
    ##Just in case you don't know how to write on a keyboard
    
    if change in no_list:               ##If it's in the list, stay in current dir
        
        current = Path.cwd()
        return(current)

    else:                               ##Else go in the chosen directory
        
        os.chdir(Path(change))          ##Change working directory
        return(Path(change))

def erase_function(dir, link):
    new_link = get_repo_name_from_url(link)
    for filename in os.listdir(dir / new_link):
        filepath = dir / new_link / filename
        try:
            shutil.rmtree(filepath, onerror= on_rm_error)
        except OSError:
            try:
                os.remove(filepath)
            except FileNotFoundError:
                pass


def get_repo_name_from_url(url: str) -> str:
    last_slash_index = url.rfind("/")
    last_suffix_index = url.rfind(".git")
    if last_suffix_index < 0:
        last_suffix_index = len(url)

    if last_slash_index < 0 or last_suffix_index <= last_slash_index:
        raise Exception("Badly formatted url {}".format(url))

    return url[last_slash_index + 1:last_suffix_index]

def on_rm_error( func, path, exc_info):
    # path contains the path of the file that couldn't be removed
    # let's just assume that it's read-only and unlink it.
    os.chmod( path, stat.S_IWRITE )
    os.unlink( path )

