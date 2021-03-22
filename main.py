from pathlib import Path
import Files.git_helper
import Files.system_reqs

if __name__ != "__main__":
    print(Path.cwd(), "is current directory")
    
    no_list = ["no", "No","nO", "NO", "False", "false", "FALSE"]
    
    change = input("Change dir?\n") ##Want to change dir?

    pos = Files.system_reqs.position_correct(change, no_list)    ##Check and eventually change dir

    Files.system_reqs.cls()

    print(Path.cwd())

    branch = input("Branchname:\n")

    Files.git_helper.change_branch(change, branch, True, True)

if __name__ != "__main__":      ##Trying to make it also as module
    yes_list = ["si", "Si","Sì", "SI", "sì"]
    no_list = ["no", "No","nO", "NO", "False", "false", "FALSE"]
    
    print(Path.cwd(), "is current directory")
    
    change = input("Change dir?\n") ##Want to change dir?

    pos = Files.system_reqs.position_correct(change, no_list)    ##Check and eventually change dir

    Files.system_reqs.cls()

    print(pos)

    link = input()
    try:
        Files.git_helper.clone_repo(link, pos)
    except:
        print("Directory "+str(pos)+" is full.")
        
        erase = input("Do you want to erase all and clone repo anyway?\n")

        if erase in yes_list:
            Files.git_helper.clone_repo(link, pos, True)

if __name__ != "__main__":
    yes_list = ["si", "Si","Sì", "SI", "sì"]
    no_list = ["no", "No","nO", "NO", "False", "false", "FALSE"]
    
    print(Path.cwd(), "is current directory")
    
    change = input("Change dir?\n") ##Want to change dir?

    pos = Files.system_reqs.position_correct(change, no_list)    ##Check and eventually change dir

    Files.system_reqs.cls()

    print(pos)

    Force = input("Do you want to force it?\n")
    if Force in yes_list:
        Files.git_helper.reset_repo(pos, True)
    elif Force in no_list:
        Files.git_helper.reset_repo(pos)

if __name__ == "__main__":
    yes_list = ["si", "Si","Sì", "SI", "sì"]
    no_list = ["no", "No","nO", "NO", "False", "false", "FALSE"]
    
    print(Path.cwd(), "is current directory")
    
    change = input("Change dir?\n") ##Want to change dir?

    pos = Files.system_reqs.position_correct(change, no_list)    ##Check and eventually change dir

    Files.system_reqs.cls()

    print(pos)

    message = input("Message")
    Force = input("Do you want to force?")
    if Force in yes_list:
        Files.git_helper.push_repo(pos,message,Force=True)
    if Force in no_list:
        Files.git_helper.push_repo(pos,message,Force=False)
    