import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
from modules.createfile import Create

init(strip=not sys.stdout.isatty())

greet = "ProxyBeautify"
cprint(figlet_format(greet, font="standard"), "blue")
 
# Create.createTxt()