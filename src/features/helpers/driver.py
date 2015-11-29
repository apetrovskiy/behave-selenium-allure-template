from .browsers import Browsers 
from helpers import configuration
import os
from selenium import webdriver

def get_chrome():
    chromedriver = configuration.read_chromedriver_location()
    os.environ["webdriver.chrome.driver"] = chromedriver
    return webdriver.Chrome(chromedriver)
    
def get_ie():
    iedriver = configuration.read_internetexplorer_location()
    os.environ["webdriver.ie.driver"] = iedriver
    return webdriver.Ie(iedriver)
    
def switch_browser(browser):
    return {
        Browsers.chrome : get_chrome,
        Browsers.internetexplorer : get_ie
    }.get(browser, lambda: webdriver.Firefox())()
   