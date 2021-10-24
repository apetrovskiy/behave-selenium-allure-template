from enum import Enum
from src.features.helpers import configuration


class Stage(Enum):
    """[summary]

    Args:
        Enum ([type]): [description]
    """
    step = 1
    feature = 2
    scenario = 3
    lifetime = 4


desiredclearance = configuration.get_setting("selenium", "clear_cookies")


def clear_cookies_if_required(entity_type, context):
    """[summary]

    Args:
        entity_type ([type]): [description]
        context ([type]): [description]
    """
    if entity_type == Stage[desiredclearance]:
        context.browser.delete_all_cookies()
        print("deleting cookies")
