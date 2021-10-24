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
# from webdriver_manager.microsoft import IeDriverManager
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
    if browser == Browsers.chrome:
        return webdriver.Chrome(ChromeDriverManager().install())
    elif browser == Browsers.chromium:
        return webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    elif browser == Browsers.firefox:
        return webdriver.Firefox(GeckoDriverManager.install())
    elif browser == Browsers.edge:
        return webdriver.Edge(EdgeChromiumDriverManager.install())
    # elif browser == Browsers.internetexplorer:
    #     return webdriver.InternetExplorer(IeDriverManager.install())
    elif browser == Browsers.opera:
        return webdriver.Opera(OperaDriverManager.install())
    else:
        return webdriver.Firefox(GeckoDriverManager.install())
