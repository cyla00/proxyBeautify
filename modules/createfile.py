import os
import requests
from modules.getdir import getDesktop

downloadLink = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all"
list = requests.get(downloadLink, allow_redirects=True)

def createTxt():
    desktop = getDesktop.dir()
    os.chdir(desktop)
    fileName = "socks5"
    fileType = ".txt"
    file = open(fileName + fileType, "wb").write(list.content)
    print(f"{file} created on {desktop}")

