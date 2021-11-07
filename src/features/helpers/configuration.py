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


def get_config():
    """[summary]

    Returns:
        [type]: [description]
    """
    config_file_path = os.path.join(projectRoot, "src", "config.ini")
    config_parser = configparser.RawConfigParser()
    config_parser.read(config_file_path)
    return config_parser


config = get_config()


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
