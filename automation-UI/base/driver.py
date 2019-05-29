"""
@package base

This is a module that implements the Singleton Driver class along with Strategy pattern DriverSelector class and
the concrete driver implementations

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.ie.options import Options as IeOptions

import globalconfig


class Driver:
    """
    Singleton Driver class to enforce one driver instance use

    Methods
    -------
    instance()
        return driver instance. Same instance if already exists

    """
    @staticmethod
    def instance():
        if '_instance' not in Driver.__dict__:
            selected_driver = DriverSelector(globalconfig.browser.lower(), globalconfig.browser_arguments)
            Driver._instance = selected_driver.get_webdriver_instance()
            Driver._instance.implicitly_wait(globalconfig.browser_implicit_wait_in_secs)
        return Driver._instance


class DriverSelector:
    """
    Driver Selector class to implement the Strategy pattern i.e. allow
    runtime selectable driver type with appropriate configuration settings

    Methods
    ------

    __init__(browser, arguments)
        instantiates appropriate driver selector specified by browser and passes the arguments
        to the driver appropriately

    get_webdriver_instance()
        selects the appropriate driver type and returns its instance
    """

    def __init__(self, browser, arguments=None):
        my_dict = {"firefox": DriverSelectorFirefox(arguments), "chrome": DriverSelectorChrome(arguments),
                   "ie": DriverSelectorIe(arguments)}
        self.strategy = my_dict[browser]

    def get_webdriver_instance(self):
        return self.strategy.get_webdriver_instance()


class DriverSelectorFirefox:
    """
    Concrete firefox driver selector class

    Methods
    ------

    __init__(arguments)
        sets up options for firefox with arguments specified

    get_webdriver_instance()
        returns firefox driver instance
    """

    def __init__(self, arguments):
        self.options = FirefoxOptions()
        self.arguments = arguments

    def get_webdriver_instance(self):
        if 'headless' in self.arguments:
            self.options.add_argument('-headless')
        ffox = webdriver.Firefox(options=self.options)
        if 'start-maximized' in self.arguments:
            ffox.maximize_window()
        return ffox


class DriverSelectorChrome:
    """
    Concrete chrome driver selector class

    Methods
    ------

    __init__(arguments)
        sets up options for chrome with arguments specified

    get_webdriver_instance()
        returns chrome driver instance
    """

    def __init__(self, arguments):
        self.options = ChromeOptions()
        self.arguments = arguments

    def get_webdriver_instance(self):
        if 'start-maximized' in self.arguments:
            self.options.add_argument('start-maximized')
        if 'headless' in self.arguments:
            self.options.add_argument('--headless')
        return webdriver.Chrome(options=self.options)


class DriverSelectorIe:
    """
    Concrete IE driver selector class

    Methods
    ------

    __init__(arguments)
        sets up options for IE with arguments specified

    get_webdriver_instance()
        returns IE driver instance
    """

    def __init__(self, arguments):
        self.options = IeOptions()
        for argument in arguments:
            self.options.add_argument(argument)

    def get_webdriver_instance(self):
        return webdriver.Ie(options=self.options)


