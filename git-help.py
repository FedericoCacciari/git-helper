from pathlib import Path
import Files.git_helper as gh
import Files.system_reqs as sr

yes_list = ["si", "Si", "sI", "Sì", "sì", "SI"]

def pos():

    print(Path.cwd(), "is current directory")
    
    change = input("Change dir?\n") ##Want to change dir?

    pos = sr.position_correct(change)    ##Check and eventually change dir

    sr.cls()

    print(Path.cwd())

    print("1.Clone Repository\n2.Change Branch\n3.Update Repository")
    
    return(Path(pos))

if __name__ == "__main__":      ##Trying to make it also as module
    position = pos()
    choice = int(input())
    if choice == 1:
        sr.cls()
        link = input("Insert link repo (SSH\\HTTPS)\n")
        try:
            gh.clone_repo(link, pos)
        except Exception:
            Force = input("Folder is Full, do you want to force clone?")
            if Force in yes_list:
                gh.clone_repo(link, pos, True)
            else:
                exit(1)
    if choice == 2:
        branchname = input("Insert Branch name:\n")
        try:
            gh.change_branch(pos, branchname)
        except:
            Force = input("Branch doesn't exist, do you want to create it?")
            if Force in yes_list:
                gh.change_branch(pos, branchname, True)
            else:
                exit(1)
    if choice == 3:
        try:
            gh.update_repo(pos)
        except Exception:
            Force = input("Your files are ahead the online Repo, do you want to reset it?\n")
            if Force in yes_list:
                gh.update_repo(pos, True)
            else:
                exit(1)