import os
import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
import requests
from proxy_checker import ProxyChecker

# from 50ms to max 10000ms
timeout = 1000 

# for all type "all" for a specific country use country code (IT, US, DE etc...)
country_link = "all"

# choose from http, socks4 and socks5
protocol_link = "http"

downloadLink = f"https://api.proxyscrape.com/v2/?request=getproxies&protocol={protocol_link}&timeout={timeout}&country={country_link}&simplified=true"
list = requests.get(downloadLink, allow_redirects=True)




class Create:

    def createTxt():

        content = list.content
        listed = content.split()

        for ip in listed:
            proxy = str(ip)

            to_scan = proxy.translate({ord("b"): None, ord("'"): None})
            cleaned = to_scan.translate({ord(":"): "  "})

            checker = ProxyChecker()
            done = checker.check_proxy(to_scan)

            if done == False:
                cprint("dead", "cyan")
            else:
                protocol = done['protocols']
                for p in protocol:
                    cleaned_protocol = p.translate({ord("["): None})

                country_code = done['country_code']
                country = done['country']
                anonymous = done['anonymity']
                timeout = done['timeout']
                cprint(f"{cleaned_protocol}  {cleaned}     ====> {country} |{country_code}|{anonymous}|timeout: ( {timeout} )", "cyan")            


