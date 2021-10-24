import configparser
import os
import sys
import platform
from .browsers import Browsers

projectRoot = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(__file__))))


def is_64bit():
    return sys.maxsize > 2**32


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
    print(os.path.join(projectRoot, "tools", get_chromedriver()))
    return os.path.join(projectRoot, "tools", get_chromedriver())


def read_internetexplorer_location():
    return os.path.join(projectRoot, "tools", "IEDriverServer.exe")


def is_windows():
    return platform.system().lower() == "windows"


def is_linux():
    return platform.system().lower() == "linux"


def get_chromedriver_file_name():
    return "chromedriver.exe" if is_windows() else "chromedriver"


def get_chromedriver():
    return f"{platform.system().lower()}/{platform.machine()}/{get_chromedriver_file_name()}"
