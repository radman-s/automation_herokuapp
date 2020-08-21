from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .locator import Locator
from .base_page import BasePage


class HerokuappPage(BasePage):

    url = 'http://the-internet.herokuapp.com/'

    # upload file
    @property
    def upload_file(self):
        locator = Locator(By.XPATH, '//a[text()="File Upload"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def choose_file(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="file-upload"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def submit_file(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="file-submit"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def validate_msg(self):
        locator = Locator(By.XPATH, '//div[@class="example"]/h3')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def uploaded_file(self):
        locator = Locator(By.CSS_SELECTOR, 'div[id="uploaded-files"]')
        return BaseElement(driver=self.driver, locator=locator)

    # drag and drop
    @property
    def drag_drop(self):
        locator = Locator(By.XPATH, '//a[text()="Drag and Drop"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def drag_a(self):
        locator = Locator(By.CSS_SELECTOR, 'div[id="column-a"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def drag_b(self):
        locator = Locator(By.CSS_SELECTOR, 'div[id="column-b"]')
        return BaseElement(driver=self.driver, locator=locator)

    # dynamic loading
    @property
    def dynamic_loading(self):
        locator = Locator(By.XPATH, '//a[text()="Dynamic Loading"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def example1(self):
        locator = Locator(By.XPATH, '//a[text()="Example 1: Element on page that is hidden"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def example2(self):
        locator = Locator(By.XPATH, '//a[text()="Example 2: Element rendered after the fact"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def start_dynamic(self):
        locator = Locator(By.XPATH, '//button[text()="Start"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def loading(self):
        locator = Locator(By.XPATH, '//div[@id="loading"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def hidden_elem(self):
        locator = Locator(By.XPATH, '//div[@id="finish"]/h4')
        return BaseElement(driver=self.driver, locator=locator)

    # exit intent
    @property
    def exit_intent(self):
        locator = Locator(By.XPATH, '//a[text()="Exit Intent"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def exit_text(self):
        locator = Locator(By.XPATH, '//div[@class="example"]/h3')
        return BaseElement(driver=self.driver, locator=locator)

    # frames
    @property
    def frames(self):
        locator = Locator(By.XPATH, '//a[text()="Frames"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def iframe_link(self):
        locator = Locator(By.XPATH, '//a[text()="iFrame"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def iframe_text(self):
        locator = Locator(By.XPATH, '//body[@id="tinymce"]/p')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def iframe_p(self):
        locator = Locator(By.CSS_SELECTOR, 'div[id="mceu_29"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def align_right(self):
        locator = Locator(By.CSS_SELECTOR, 'i[class="mce-ico mce-i-alignright"]')
        return BaseElement(driver=self.driver, locator=locator)

    # horizontal slider
    @property
    def horizont_slider_link(self):
        locator = Locator(By.XPATH, '//a[text()="Horizontal Slider"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def horizont_slider(self):
        locator = Locator(By.XPATH, '//div[@class="sliderContainer"]/input')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def slider_range(self):
        locator = Locator(By.CSS_SELECTOR, 'span[id="range"]')
        return BaseElement(driver=self.driver, locator=locator)



    # new window
    @property
    def muliple_windows(self):
        locator = Locator(By.XPATH, '//a[text()="Multiple Windows"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def click_here(self):
        locator = Locator(By.XPATH, '//a[text()="Click Here"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def text_new_window(self):
        locator = Locator(By.XPATH, '//h3[text()="New Window"]')
        return BaseElement(driver=self.driver, locator=locator)






