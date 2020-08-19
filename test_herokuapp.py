from pages.drivers import Drivers
from pages.herokuapp_page import HerokuappPage
from pages.base_element import BaseElement
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = Drivers('--start').chrome()
hp = HerokuappPage(driver=browser)

hp.go()
hp.drag_drop.click()

a = browser.find_element_by_css_selector('div[id="column-a"]')
b = browser.find_element_by_css_selector('div[id="column-b"]')

time.sleep(2)
move = ActionChains(browser)
move.drag_and_drop(b, a)

# in progress....





