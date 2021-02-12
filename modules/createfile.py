import os
import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
import requests

downloadLink = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all"
list = requests.get(downloadLink, allow_redirects=True)


class Create:

    def createTxt():

        content = list.content
        listed = content.split()

        for ip in listed:
            proxy = str(ip)
            cleaned = proxy.translate({ord("b"): None, ord("'"): None, ord(":"): " "})
            cprint(f"socks5 {cleaned}", "cyan")            


