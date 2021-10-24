"""[summary]

    Returns:
        [type]: [description]
    """
from enum import Enum


class Browsers(Enum):
    """List of supported browsers

    Args:
        Enum ([type]): [description]

    Returns:
        [type]: [description]
    """
    CHROME = 1
    FIREFOX = 2
    INTERNET_EXPLORER = 3
    phantom = 4
    opera = 5
    edge = 6
    chromium = 7

    @classmethod
    def get_browser(self, b):
        """Returns a Browsers value by input string

        Args:
            b (string): textual name of browser

        Returns:
            Browsers: enumeration
        """
        return {
            "Chrome": self.CHROME,
            "Google Chrome": self.CHROME,
            "Firefox": self.FIREFOX,
            "FireFox": self.FIREFOX,
            "Internet Explorer": self.INTERNET_EXPLORER,
            "IE": self.INTERNET_EXPLORER,
            "Phantom": self.phantom,
            "Edge": self.edge,
            "Chromium": self.chromium,
            "Opera": self.opera
        }[b]
