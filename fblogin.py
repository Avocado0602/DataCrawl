from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# 1. Khai báo biến browser
browser = webdriver.Chrome(executable_path="./chromedriver.exe")

# 2. Mở thử một trang web
browser.get("http://facebook.com")

# 2a. Điền thông tin vào ô user và pass
txtUser = browser.find_element("name", "email")
txtUser.send_keys("tainguyenavo06022001@gmail.com")

txtPass = browser.find_element("name", "pass")
txtPass.send_keys("Avocado06022001@")

# 2b. Submit form
txtPass.send_keys(Keys.ENTER)

# 3. Dừng chương trình 5s
sleep(5)

# 4. Đóng trình duyệt
browser.close()