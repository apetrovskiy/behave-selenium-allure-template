"""[summary]
    """
from behave import step
from behave.model import Feature, Scenario
from behave.runner import Context
from src.features.helpers.browsers import Browsers
from src.features.helpers import configuration
from src.features.helpers import driver
from src.features.helpers import screenshot
from src.features.helpers import session


def before_step(context: Context, step: step):
    """[summary]

    Args:
        context (Context): [description]
        step (step): [description]
    """
    # Runs before each Given, When and Then step.
    pass


def after_step(context: Context, step: step):
    """[summary]

    Args:
        context (Context): [description]
        step (step): [description]
    """
    session.clear_cookies_if_required(session.Stage.STEP, context)
    # Runs after each step.
    if step.status == "failed":
        print("step failed")


def before_scenario(context: Context, scenario: Scenario):
    """[summary]

    Args:
        context (Context): [description]
        scenario (Scenario): [description]
    """
    # Runs before each full scenario (complete Given, When, Then definition)
    pass


def after_scenario(context: Context, scenario: Scenario):
    """[summary]

    Args:
        context (Context): [description]
        scenario (Scenario): [description]
    """
    session.clear_cookies_if_required(session.Stage.SCENARIO, context)
    # Runs after each scenario
    if scenario.status == "failed":
        screenshot.capture_failure(context, scenario)


def before_feature(context: Context, feature: Feature):
    """[summary]

    Args:
        context (Context): [description]
        feature (Feature): [description]
    """
    # Runs before each feature file
    pass


def after_feature(context: Context, feature: Feature):
    """[summary]

    Args:
        context (Context): [description]
        feature (Feature): [description]
    """
    session.clear_cookies_if_required(session.Stage.FEATURE, context)
    # Runs after each feature
    pass


def before_all(context: Context):
    """[summary]

    Args:
        context (Context): [description]
    """
    browsertype: Browsers = configuration.get_browser()
    context.browser = driver.switch_browser(browsertype)


def after_all(context: Context):
    """[summary]

    Args:
        context (Context): [description]
    """
    session.clear_cookies_if_required(session.Stage.LIFETIME, context)
    # Very last thing to run.
    context.browser.quit()
