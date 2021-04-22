from Proxy_List_Scrapper import Scrapper, Proxy, ScrapperException
from proxy_checker import ProxyChecker
from termcolor import cprint
from pyfiglet import figlet_format
from threading import Thread
from modules.url0 import *
from modules.choices import *

# aesthetics in terminal
greet = "ProxyBeautify"
cprint(figlet_format(greet), "cyan")
owner = "we are all mad here"
cprint(figlet_format(owner, font="digital"), "cyan")

################################################################################
format_choice = Choices.format()

cprint('the slaves are working, avg proxies to check (5k), this may take a while...', "cyan")
print('')

if __name__ == '__main__':
    Thread(target = URLS.scrap0(format_choice)).start()
    Thread(target = URLS.scrap1(format_choice)).start()
    Thread(target = URLS.scrap2(format_choice)).start()
    Thread(target = URLS.scrap3(format_choice)).start()
