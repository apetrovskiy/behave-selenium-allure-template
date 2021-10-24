import os
from src.features.helpers import configuration


def capture_failure(context, scenario):
    """[summary]

    Args:
        context ([type]): [description]
        scenario ([type]): [description]
    """
    originalpath = os.getcwd()
    path = os.path.join(configuration.projectRoot, "failures")
    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)
    context.browser.maximize_window()
    context.browser.save_screenshot(scenario.name + ".png")
    os.chdir(originalpath)
