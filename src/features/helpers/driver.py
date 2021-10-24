from .browsers import Browsers
from helpers import configuration
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from webdriver_manager.microsoft import IeDriverManager
from webdriver_manager.opera import OperaDriverManager


def switch_browser(browser: Browsers) -> str:
    return {
        Browsers.chrome: webdriver.Chrome(ChromeDriverManager().install()),
        # Browsers.chromium: webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),
        # Browsers.firefox: webdriver.Firefox(GeckoDriverManager.install()),
        # Browsers.internetexplorer: IeDriverManager.install(),
        # Browsers.edge: webdriver.Edge(EdgeChromiumDriverManager.install()),
        # Browsers.opera: webdriver.Opera(OperaDriverManager.install()),
    }.get(browser, lambda: webdriver.Firefox())
