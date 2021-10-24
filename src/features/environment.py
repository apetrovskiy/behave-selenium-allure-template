from behave import step
from behave.model import Feature, Scenario
from behave.runner import Context
from src.features.helpers.browsers import Browsers
from helpers import configuration
from helpers import driver
from helpers import screenshot
from helpers import session


def before_step(context: Context, step: step):
    # Runs before each Given, When and Then step.
    pass


def after_step(context: Context, step: step):
    session.clear_cookies_if_required(session.Stage.step, context)
    # Runs after each step.
    if step.status == "failed":
        print("step failed")


def before_scenario(context: Context, scenario: Scenario):
    # Runs before each full scenario (complete Given, When, Then definition)
    pass


def after_scenario(context: Context, scenario: Scenario):
    session.clear_cookies_if_required(session.Stage.scenario, context)
    # Runs after each scenario
    if scenario.status == "failed":
        screenshot.capture_failure(context, scenario)


def before_feature(context: Context, feature: Feature):
    # Runs before each feature file
    pass


def after_feature(context: Context, feature: Feature):
    session.clear_cookies_if_required(session.Stage.feature, context)
    # Runs after each feature
    pass


def before_all(context: Context):
    browsertype: Browsers = configuration.get_browser()
    context.browser = driver.switch_browser(browsertype)


def after_all(context: Context):
    session.clear_cookies_if_required(session.Stage.lifetime, context)
    # Very last thing to run.
    context.browser.quit()
