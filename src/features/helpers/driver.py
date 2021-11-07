"""[summary]

    Returns:
        [type]: [description]
    """
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.opera import OperaDriverManager
from src.features.helpers.browsers import Browsers
from src.features.helpers import configuration


def switch_browser(browser: Browsers) -> str:
    """[summary]

    Args:
        browser (Browsers): [description]

    Returns:
        str: [description]
    """
    if browser == Browsers.CHROME:
        return webdriver.Chrome(ChromeDriverManager().install())
    elif browser == Browsers.CHROMIUM:
        return webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    elif browser == Browsers.FIREFOX:
        return webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == Browsers.EDGE:
        # return webdriver.Edge(EdgeChromiumDriverManager.install())
        return webdriver.Edge(EdgeChromiumDriverManager().install())
    elif browser == Browsers.internetexplorer:
        return webdriver.Ie(IEDriverManager().install())
    elif browser == Browsers.OPERA:
        return webdriver.Opera(executable_path=OperaDriverManager().install())
    else:
        return webdriver.Firefox(executable_path=GeckoDriverManager().install())
