from pathlib import Path
import Files.git_helper
import Files.system_reqs

if __name__ == "__main__":
    print(Path.cwd(), "is current directory")
    
    change = input("Change dir?\n") ##Want to change dir?

    pos = Files.system_reqs.position_correct(change)    ##Check and eventually change dir

    Files.system_reqs.cls()

    print(Path.cwd())

    branch = input("Branchname:\n")

    Files.git_helper.change_branch(change, branch, True, True)

if __name__ != "__main__":      ##Trying to make it also as module
    yes_list = ["si", "Si","Sì", "SI", "sì"]
    
    print(Path.cwd(), "is current directory")
    
    change = input("Change dir?\n") ##Want to change dir?

    pos = Files.system_reqs.position_correct(change)    ##Check and eventually change dir

    Files.system_reqs.cls()

    print(pos)

    link = input()

    First = Files.git_helper.clone_repo(link, pos, returner=True)

    if First == False:
        
        print("Directory "+str(pos)+" is full.")
        
        erase = input("Do you want to erase all and clone repo anyway?\n")

        if erase in yes_list:
            second = Files.git_helper.clone_repo(link, pos, True, True)
            
            if second == True:
                print("Fatto")
            
            else:
                print("Errore")
