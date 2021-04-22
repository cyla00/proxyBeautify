from termcolor import cprint
import threading
import time
from .choices import *

class Checker:

    def single_check(raw_list, checker, format_choice):

        for raw_ips in raw_list:
            checked_ips = checker.check_proxy(raw_list)

            if checked_ips != False:
                raw_protocol = checked_ips['protocols']
                for i in raw_protocol:
                    protocol = i.replace('[]',"")

                anonymity = checked_ips['anonymity']
                country = checked_ips['country']
                country_code = checked_ips['country_code']
                timeout = checked_ips['timeout']

                proxychains_raw_ip = raw_ips.replace(':', '  ')
                Choices.ouput_format(proxychains_raw_ip, protocol, raw_ips, anonymity, timeout, country, country_code, format_choice)

    def multi_check(raw_list, checker, format_choice):

        for raw_ips in raw_list:
            checked_ips = checker.check_proxy(raw_ips)

            if checked_ips != False:
                raw_protocol = checked_ips['protocols']
                for i in raw_protocol:
                    protocol = i.replace('[]',"")

                anonymity = checked_ips['anonymity']
                country = checked_ips['country']
                country_code = checked_ips['country_code']
                timeout = checked_ips['timeout']
                proxychains_raw_ip = raw_ips.replace(':', '  ')
                Choices.ouput_format(proxychains_raw_ip, protocol, raw_ips, anonymity, timeout, country, country_code, format_choice)
