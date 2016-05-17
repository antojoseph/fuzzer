import os
import banner
import gen_data
import run_campaign

def welcome_banner():
    banner.horizontal("DroiD-FF")


def error():
    os.system('clear')
    print "Invalid Data , Try Again !"
    show_options()


def show_options():
    options = ['(0) Generate Files', '(1) Start running fuzzer', '(2) View Crashes', '(3) Triage Crashes']

    for x in range(len(options)):
        print "     " + options[x]

    try:
        user_selection = raw_input("Please enter your selection  : ")
        if (int(user_selection) >= len(options)):
            error()
        else:
            print "Your Option is : " + options[int(user_selection)]
            if int(user_selection) == 0:
                gen_data.fuzzer_options()
            elif int(user_selection) ==1 :
                run_campaign.start()
    except ValueError:
        error()


welcome_banner()
show_options()
