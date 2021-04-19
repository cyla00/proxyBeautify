# website reference 'https://spys.one/en/free-proxy-list/'

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
import time
import os
import re

class List_1:

    def scrap():

        ####### get's website URL
        firefoxOptions = Options()
        firefoxOptions.add_argument("-headless")
        website = webdriver.Firefox(executable_path="./drivers/geckodriver", options=firefoxOptions)
        website.get('https://spys.one/en/free-proxy-list/')

        ####### makes sure that 500 lenght result is selected
        website.implicitly_wait(10)
        select_500 = Select(website.find_element_by_id("xpp"))
        select_500.select_by_visible_text("500")
        website.implicitly_wait(10)
        check_500 = Select(website.find_element_by_id("xpp"))
        check_500.select_by_visible_text("500")

        ####### fetch the list of IPs plus info and sanitize
        get_ip = website.find_elements_by_class_name("spy14")
        for i in get_ip:
            whitelist = set('1234567890:.')
            re_ip = re.compile('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5})')
            raw_ip_list = re.findall(re_ip, str(i.text))
            if raw_ip_list == '':
                raw_ip_list.remove()
            to_scan = ''.join(raw_ip_list)
            print(str(to_scan))

        website.quit()














ciao = List_1.scrap()
