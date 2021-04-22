from Proxy_List_Scrapper import Scrapper, Proxy, ScrapperException
from proxy_checker import ProxyChecker
from termcolor import cprint
from pyfiglet import figlet_format
from threading import Thread
from concurrent.futures import ProcessPoolExecutor
from modules.url0 import *
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

if __name__ == '__main__':


    with ProcessPoolExecutor(4) as executor:
        exec1 = executor.submit(URLS.scrap0(format_choice), 1)
        exec2 = executor.submit(URLS.scrap1(format_choice), 2)
        exec3 = executor.submit(URLS.scrap2(format_choice), 3)
        exec4 = executor.submit(URLS.scrap3(format_choice), 4)

        exec1.result()
        exec2.result()
        exec3.result()
        exec4.result()
    # Thread(target = URLS.scrap0(format_choice)).start()
    # Thread(target = URLS.scrap1(format_choice)).start()
    # Thread(target = URLS.scrap2(format_choice)).start()
    # Thread(target = URLS.scrap3(format_choice)).start()
