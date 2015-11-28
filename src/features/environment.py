import os
from selenium import webdriver

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
    # Very first thing to run before all features, scenarios and steps.
    root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    chromedriver = os.path.join(root, "tools", "chromedriver.exe")
    os.environ["webdriver.chrome.driver"] = chromedriver
    
    print(chromedriver)
    
    print("I run before everything, set up the browser here")
    context.browser = webdriver.Chrome(chromedriver)

def after_all(context):
    # Very last thing to run.
    context.browser.quit()