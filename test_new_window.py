from pages.drivers import Drivers
from pages.herokuapp_page import HerokuappPage
import time


browser = Drivers('--start-').chrome()
hp = HerokuappPage(driver=browser)

# test start
window_before = browser.window_handles[0]
window_after = browser.window_handles[1]


hp.go()
hp.muliple_windows.click()
hp.click_here.click()
browser.switch_to_window(window_after)
tx_new = hp.text_new_window.text
print(tx_new)

