"""[summary]

    Returns:
        [type]: [description]
    """
import configparser
import os
import sys
from src.features.helpers.browsers import Browsers

projectRoot = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(__file__))))


def is_64bit():
    """[summary]

    Returns:
        [type]: [description]
    """
    return sys.maxsize > 2**32


def getConfig():
    """[summary]

    Returns:
        [type]: [description]
    """
    configFilePath = os.path.join(projectRoot, "src", "config.ini")
    configParser = configparser.RawConfigParser()
    configParser.read(configFilePath)
    return configParser


config = getConfig()


def get_setting(parent, key):
    """[summary]

    Args:
        parent ([type]): [description]
        key ([type]): [description]

    Returns:
        [type]: [description]
    """
    return config.get(parent, key)


def get_browser():
    """[summary]

    Returns:
        [type]: [description]
    """
    return Browsers.get_browser(get_setting("selenium", "driver"))
