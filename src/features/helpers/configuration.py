import configparser
import os
import sys
from src.features.helpers.browsers import Browsers

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
