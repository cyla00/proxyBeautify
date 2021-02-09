import os
from modules.getdir import getDesktop
 
def createTxt():
    desktop = getDesktop.dir()
    os.chdir(desktop)
    file = open("test.txt", "x")
    print(f"{file.name} created on {desktop}")