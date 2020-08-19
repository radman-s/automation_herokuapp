from pages.drivers import Drivers
from pages.herokuapp_page import HerokuappPage


browser = Drivers('--start-').chrome()
hp = HerokuappPage(driver=browser)

# test start
hp.go()
hp.frames.click()
hp.iframe_link.click()
iframe = browser.find_elements_by_css_selector('div[id="mceu_13"]')

browser.switch_to_frame(iframe)
itext = hp.iframe_text.text
browser.switch_to.default_content()
print(itext)


