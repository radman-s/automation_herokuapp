from pages.drivers import Drivers
from pages.herokuapp_page import HerokuappPage



browser = Drivers('--start-maximized').chrome()
hp = HerokuappPage(driver=browser)

# test setup
expect_max = '5'
expect_min = '0'


# test start
hp.go()
hp.horizont_slider_link.click()

# move slider from 0 to maximum of 5
hp.horizont_slider.drag_offset(55,0)
max = hp.slider_range.text
assert expect_max == max
print(f'expected maximum at: {expect_max} finish at: {max}')

# move slider back from maximum to 0
hp.horizont_slider.drag_offset(-55,0)
min = hp.slider_range.text
assert expect_min == min
print(f'expected minimum at: {expect_min} finish at: {min}')
print('test passed')
browser.quit()











