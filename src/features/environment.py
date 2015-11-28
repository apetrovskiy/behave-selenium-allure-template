import os
from selenium import webdriver
from helpers import configuration
from helpers.browsers import Browsers

def before_step(context, step):
    # Runs before each Given, When and Then step.
    pass

def after_step(context, step):
    # Runs after each step.
    if step.status == "failed":
        print("step failed")
    pass

def before_scenario(context, scenario):
    # Runs before each full scenario (complete Given, When, Then definition)
    pass

def after_scenario(context, scenario):
    # Runs after each scenario
    pass

def before_feature(context, feature):
    # Runs before each feature file
    pass

def after_feature(context, feature):
    # Runs after each feature
    pass

def before_all(context):
    root = get_root()
    browsertype = configuration.read_browser(configuration.read_configuration_location(root))
    
    print("I run before everything, set up the browser here")
    context.browser = switch_browser(browsertype)

def after_all(context):
    # Very last thing to run.
    context.browser.quit()
    
def get_root():
    return configuration.read_project_root(os.path.dirname(__file__))
    
def get_chrome():
    chromedriver = configuration.read_chromedriver_location(get_root())
    os.environ["webdriver.chrome.driver"] = chromedriver
    return webdriver.Chrome(chromedriver)
    
def get_ie():
    iedriver = configuration.read_internetexplorer_location(get_root())
    os.environ["webdriver.ie.driver"] = iedriver
    return webdriver.Ie(iedriver)
    
def switch_browser(browser):
    return {
        Browsers.chrome : get_chrome,
        Browsers.internetexplorer : get_ie
    }.get(browser, lambda: webdriver.Firefox())()
   
