from pages.drivers import Drivers
from pages.herokuapp_page import HerokuappPage


browser = Drivers('--start-maximized').chrome()
hp = HerokuappPage(driver=browser)

hp.go()
hp.dynamic_loading.click()
hp.example1.click()
hp.start_dynamic.click()
progress = hp.loading.text
print(f'{progress} in progress')
hp.loading.wait_close()
print('loading finished')
hidden_element = hp.hidden_elem.text
print(f'hidden element laoded: {hidden_element}')
print('test passed')



