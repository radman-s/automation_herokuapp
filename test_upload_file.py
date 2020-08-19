from pages.drivers import Drivers
from pages.herokuapp_page import HerokuappPage

browser = Drivers('--start-maximized').chrome()
hp = HerokuappPage(driver=browser)

image_file = r'C:\Users\radss\PycharmProjects\automation_herokuapp\image\images.png'
expected_scs_msg = 'File Uploaded!'

# test start
hp.go()
hp.upload_file.click()
hp.choose_file.input_text(image_file)
hp.submit_file.click()
scs_msg = hp.validate_msg.text
assert expected_scs_msg == scs_msg
print(scs_msg)
browser.quit()
print('test passed')

