"""[summary]
    """
from enum import Enum
from src.features.helpers import configuration


class Stage(Enum):
    """[summary]

    Args:
        Enum ([type]): [description]
    """
    STEP = 1
    FEATURE = 2
    SCENARIO = 3
    LIFETIME = 4


desiredclearance = configuration.get_setting("selenium", "clear_cookies")


def clear_cookies_if_required(entity_type, context):
    """[summary]

    Args:
        entity_type ([type]): [description]
        context ([type]): [description]
    """
    if entity_type == Stage[desiredclearance.upper()]:
        context.browser.delete_all_cookies()
        print("deleting cookies")
