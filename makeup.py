import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
from modules.createfile import Create

init(strip=not sys.stdout.isatty())

greet = "ProxyBeautify"
cprint(figlet_format(greet), "cyan")
owner = "by seroktika"
cprint(figlet_format(owner, font="digital"), "cyan")



def program():

    cprint('dump? y or exit', "cyan")
    answer = input()

    if answer == 'y':
        try:
            Create.createTxt()
        except:
            cprint('error occured please try later', "cyan")
            program()
    elif answer == 'exit':
            cprint('exiting...', "cyan")
    else:
        cprint("############ bro don't waste my time ############", "cyan")
        program()
        
program()