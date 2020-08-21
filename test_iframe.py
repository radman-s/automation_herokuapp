from pages.drivers import Drivers
from pages.herokuapp_page import HerokuappPage
import time


browser = Drivers('--start-').chrome()
hp = HerokuappPage(driver=browser)

content = 'My automation test content'

# test start
hp.go()
hp.frames.click()
hp.iframe_link.click()

iframe = browser.find_element_by_tag_name('iframe')
browser.switch_to_frame(iframe)
itext = hp.iframe_text.text
hp.iframe_text.input_text(content)
hp.align_right.click()



# browser.switch_to.default_content()
print(itext)


