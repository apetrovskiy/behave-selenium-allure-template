from helpers import configuration
from helpers import driver
from helpers import screenshot
from helpers import session

def before_step(context, step):
    # Runs before each Given, When and Then step.
    pass

def after_step(context, step):
    session.clear_cookies_if_required(session.Stage.step, context)
    # Runs after each step.
    if step.status == "failed":
        print("step failed")

def before_scenario(context, scenario): 
    # Runs before each full scenario (complete Given, When, Then definition)
    pass

def after_scenario(context, scenario):
    session.clear_cookies_if_required(session.Stage.scenario, context)
    # Runs after each scenario
    if scenario.status == "failed":
        screenshot.capture_failure(context, scenario)

def before_feature(context, feature):
    # Runs before each feature file
    pass

def after_feature(context, feature):
    session.clear_cookies_if_required(session.Stage.feature, context)
    # Runs after each feature
    pass

def before_all(context):
    browsertype = configuration.get_browser()
    context.browser = driver.switch_browser(browsertype)

def after_all(context):
    session.clear_cookies_if_required(session.Stage.lifetime, context)
    # Very last thing to run.
    context.browser.quit()
