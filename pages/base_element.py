from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select



class BaseElement(object):

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    def click(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator=self.locator))
        element.click()
        return None

    def input_text(self, text):
        self.web_element.send_keys(text)
        return None

    @property
    def text(self):
        text = self.web_element.text
        return text

    def drag_drop(self, source, target):
        element = ActionChains(self.driver)
        element.drag_and_drop(source, target)
        return None

    def drag_offset(self, x, y):
        element = ActionChains(self.driver)
        element.click_and_hold(self.web_element).move_by_offset(x, y).release().perform()

    def context_click(self):
        element = ActionChains(self.driver)
        element.context_click().perform()
        return None

    def select_dropdown(self, val):
        element = Select(self.web_element)
        element.select_by_value(val)
        return None

    def wait_close(self):
        element = WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None













