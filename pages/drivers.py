from selenium import webdriver

class Drivers:

    def __init__(self, argument1):
        self.argument = argument1

    def chrome(self):
        options = webdriver.ChromeOptions()
        options.add_argument(self.argument)
        driver = webdriver.Chrome(options=options)
        return driver