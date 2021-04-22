from Proxy_List_Scrapper import Scrapper, Proxy, ScrapperException
from proxy_checker import ProxyChecker
from termcolor import cprint
from pyfiglet import figlet_format
from threading import Thread
from concurrent.futures import ProcessPoolExecutor
from modules.url0 import *
import sys
from modules.choices import *

# aesthetics in terminal
greet = "ProxyBeautify"
cprint(figlet_format(greet), "cyan")
owner = "we are all mad here"
cprint(figlet_format(owner, font="digital"), "cyan")

################################################################################
format_choice = Choices.format()

print('')
cprint('the slaves are working, avg proxies to check (5k), this may take a while...', "cyan")
print('')

def execution():
    with ProcessPoolExecutor(4) as executor:
        exec1 = executor.map(URLS.scrap0(format_choice), range(10000), chunksize=100)
        exec2 = executor.map(URLS.scrap1(format_choice), range(10000), chunksize=100)
        exec3 = executor.map(URLS.scrap2(format_choice), range(10000), chunksize=100)
        exec4 = executor.map(URLS.scrap3(format_choice), range(10000), chunksize=100)

        list(exec1)
        list(exec2)
        list(exec3)
        list(exec4)

if __name__ == '__main__':
    execution()
