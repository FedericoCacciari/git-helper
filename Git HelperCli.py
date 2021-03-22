from pathlib import Path
import Files.git_helper as gh
import Files.system_reqs as sr


def start():
    print(Path.cwd(), "is current directory")
    
    no_list = ["no", "No","nO", "NO", "False", "false", "FALSE"]
    
    change = input("Change dir?\n") ##Want to change dir?

    pos = sr.position_correct(change, no_list)    ##Check and eventually change dir

    sr.cls()

    print(Path.cwd())

    return(pos)

if __name__ == "__main__":

    yes_list = ["si", "Si","Sì", "SI", "sì"]

    print("1. Clone Repository\n2.Change Branch\n3.Update Repository\n4.Push Repository, \n 5.Reset Repository")

    whattodo = (input("What do you want to do?\n"))
    
    if whattodo == "exit":
        exit(0)


    pos = start()

    if whattodo == "1":
        url = input("Insert Link: ")
        try:
            gh.clone_repo(url, pos)
        except:
            Forceit = input("The folder is not Empty, do you want to Force it?")
            if Forceit in yes_list:
                gh.clone_repo(url, pos, True)
                print("Done")
            else:
                exit(1)
    
    if whattodo == "2":
        branch_name = input("Insert Branch name: ")
        gh.change_branch(pos, branch_name)
        print("Done")
    
    if whattodo == "3":
        gh.reset_repo(pos)
        print("Done")
    
    if whattodo == "4":
        message = input("Insert here the commit's message")
        Forceit = input("Do you want to force it? \nPay Attention, please")
        if Forceit in yes_list:
            gh.push_repo(pos, message, Force=True)
        else:
            gh.push_repo(pos, message)        

    if whattodo == "5":
        gh.reset_repo(pos, True)
        print("Done")
    
    input()