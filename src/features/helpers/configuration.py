import configparser
import os
from .browsers import Browsers

projectRoot = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

def getConfig():
    configFilePath = os.path.join(projectRoot, "src", "config.ini")
    configParser = configparser.RawConfigParser()
    configParser.read(configFilePath)
    return configParser

config = getConfig()

def get_setting(parent, key):
    return config.get(parent, key)

def get_browser():
    return Browsers.get_browser(get_setting("selenium", "driver"))
    
def read_chromedriver_location():
    return os.path.join(projectRoot, "tools", "chromedriver.exe")

def read_internetexplorer_location():
    return os.path.join(projectRoot, "tools", "IEDriverServer.exe")