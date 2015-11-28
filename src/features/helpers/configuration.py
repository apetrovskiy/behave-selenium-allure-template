import configparser
import os
from .browsers import Browsers

def read_browser(configFilePath):
    browsers = {
        "Chrome": Browsers.chrome, 
        "Google Chrome": Browsers.chrome,
        "Firefox" : Browsers.firefox,
        "FireFox" : Browsers.firefox,
        "Internet Explorer" : Browsers.internetexplorer,
        "IE" : Browsers.internetexplorer,
        "Phantom" : Browsers.phantom
        }
    configParser = configparser.RawConfigParser()
    configParser.read(configFilePath)
    return browsers[configParser.get("selenium", "driver")]
   
def read_project_root(currentFilePath):
    return os.path.dirname(os.path.dirname(currentFilePath))
    
def read_chromedriver_location(projectRoot):
    return os.path.join(projectRoot, "tools", "chromedriver.exe")

def read_internetexplorer_location(projectRoot):
    return os.path.join(projectRoot, "tools", "IEDriverServer.exe")
 
def read_configuration_location(projectRoot):
    return os.path.join(projectRoot, "src", "config.ini")