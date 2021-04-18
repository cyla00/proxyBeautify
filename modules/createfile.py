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
            check_int = int(timeout)
            if 25 <= check_int <= 10000:
                return timeout
            else:
                cprint("!!! choose a valid input !!!", "cyan")
                return timeout_set()

        def formattation():
            cprint("choose an output format", "cyan")
            cprint("[1] full format", "cyan")
            cprint("[2] proxychains format (type:ip:port)", "cyan")
            print_input_format = input()
            return print_input_format

        protocol_link = protocol_set()
        timeout = timeout_set()
        country_link = "all"



        downloadLink = f"https://api.proxyscrape.com/v2/?request=getproxies&protocol={protocol_link}&timeout={timeout}&country={country_link}&simplified=true"
        list = requests.get(downloadLink, allow_redirects=True)

        content = list.content
        listed = content.split()

        output_format = formattation()

        for ip in listed:

            proxy = str(ip)

            to_scan = proxy.translate({ord("b"): None, ord("'"): None})
            cleaned = to_scan.translate({ord(":"): "  "})

            checker = ProxyChecker()
            done = checker.check_proxy(to_scan)

            if done != False:

                protocol = done['protocols']
                for p in protocol:
                    cleaned_protocol = p.translate({ord("["): None})

                country_code = done['country_code']
                country = done['country']
                anonymous = done['anonymity']
                timeout = done['timeout']



                if output_format == '1':
                    cprint(f"{cleaned_protocol}:{cleaned} ====> {country}|{country_code}|{anonymous}|timeout: ( {timeout} )", "cyan")
                elif output_format == '2':
                    cprint(f"{cleaned_protocol}  {cleaned}", "cyan")
                else:
                    cprint(f"!!! choose a valid option !!!", "cyan")
                    scrap()
