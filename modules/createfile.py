import os
import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
import requests
from proxy_checker import ProxyChecker






class Create:

    def scrap():

        # choose from protocol
        def protocol_set():
            cprint("choose a protocol: socks5 | socks4 | http", "cyan")
            protocol_list = ['socks5', 'socks4', 'http']
            protocol_answer = input()


            if protocol_answer == protocol_list[0]:
                return protocol_list[0]

            elif protocol_answer == protocol_list[1]:
                return protocol_list[1]

            elif protocol_answer == protocol_list[2]:
                return protocol_list[2]
            else:
                cprint("!!! choose a valid input !!!", "cyan")
                return protocol_set()

        #choose timeout
        def timeout_set():
            cprint("choose timeout (25 to 10000)", "cyan")
            timeout = input()
            if timeout >= '25' or timeout <= '10000':
                return timeout
            else:
                cprint("!!! choose a valid input !!!", "cyan")
                return timeout_set()

        protocol_link = protocol_set()
        timeout = timeout_set()
        country_link = "all"

        downloadLink = f"https://api.proxyscrape.com/v2/?request=getproxies&protocol={protocol_link}&timeout={timeout}&country={country_link}&simplified=true"
        list = requests.get(downloadLink, allow_redirects=True)

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
