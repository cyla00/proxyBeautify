from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from proxy_checker import ProxyChecker
from termcolor import cprint
import requests
import time
import os
import re



# websites list, some have multiple pages
URL0 = [
'https://www.sslproxies.org/',
'https://free-proxy-list.net/anonymous-proxy.html',
'https://free-proxy-list.net/uk-proxy.html',
'https://www.us-proxy.org/'
]

URL1 = [
'https://www.proxy-list.download/HTTP',
'https://www.proxy-list.download/HTTPS',
'https://www.proxy-list.download/SOCKS4',
'https://www.proxy-list.download/SOCKS5'
]

URL2 = 'http://spys.me/proxy.txt'
URL3 = 'https://api.proxyscrape.com/?request=getproxies&proxytype=all&country=all&ssl=all&anonymity=all'
URL4 = 'https://spys.one/en/free-proxy-list/'

# selenium options
firefoxOptions = Options()
firefoxOptions.add_argument("-headless")
firefoxWebDriver_path = "./geckodriver"


class URLS:

    def scrap0():
        for url0index in URL0:
            website = webdriver.Firefox(executable_path=firefoxWebDriver_path, options=firefoxOptions)
            website.get(url0index)
            open_list = website.find_element_by_tag_name('textarea').get_attribute('value')
            re_ip = re.compile('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5})')
            raw_list = re.findall(re_ip, open_list)

            checker = ProxyChecker()
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

                    cprint(f"{protocol} {raw_ips}  ==> {anonymity}|timeout({timeout})     |{country}|({country_code})", 'cyan')


    def scrap1():
        for url1index in URL1:
            website = webdriver.Firefox(executable_path=firefoxWebDriver_path, options=firefoxOptions)
            website.get(url1index)
            open_list = website.find_element_by_tag_name('textarea').get_attribute('value')
            re_ip = re.compile('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5})')
            raw_list = re.findall(re_ip, open_list)
            checker = ProxyChecker()
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

                    cprint(f"{protocol} {raw_ips}  ==> {anonymity}|timeout({timeout})     |{country}|({country_code})", 'cyan')


    def scrap2():
        website = webdriver.Firefox(executable_path=firefoxWebDriver_path, options=firefoxOptions)
        website.get(URL2)
        open_list = website.find_element_by_tag_name('body').get_attribute('innerHTML')
        re_ip = re.compile('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5})')
        raw_list = re.findall(re_ip, open_list)
        checker = ProxyChecker()
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

                cprint(f"{protocol} {raw_ips}  ==> {anonymity}|timeout({timeout})     |{country}|({country_code})", 'cyan')

    def scrap3():
        website = requests.get(URL3).text
        re_ip = re.compile('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5})')
        raw_list = re.findall(re_ip, website)
        checker = ProxyChecker()
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

                cprint(f"{protocol} {raw_ips}  ==> {anonymity}|timeout({timeout})     |{country}|({country_code})", 'cyan')
