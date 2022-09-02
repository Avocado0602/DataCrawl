from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
# 1. Khai báo browser
browser = webdriver.Chrome(executable_path="./chromedriver.exe")

# 2. Mở URL của post
browser.get("https://www.facebook.com/TomorrowMarketers/posts/pfbid0QTDhMBULHU49g54EoTcTZet2vMdK4bkCgrwNK4oK7hyg7vzVzvQFQPfJKaiHavLbl?__cft__[0]=AZXT4LNpP5qHikd9ETJ9RidOArvLbEvgXa68kzFjMyLUHlQZQmMbAs37Abc4QCq_hSGTVsc2qaY4uTogghtgJbO7j-lH06jJ53sQwTg7uHkksH9FzkUr5ehsIGd72jOi3cljhJ31CNPD8_nsOgpQU9qtQPI1BT36NdNEFaqxj6k_fMgxbKxfgCXUcmn5AUS5qS8&__tn__=%2CO%2CP-R")
sleep(random.randint(5,10))

# 3. Lấy link hiện comment
showcomment_link = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/div[1]/div/div[3]/span[1]")
showcomment_link.click()
sleep(random.randint(5,10))

# 4. Lấy comment
showmore_link = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div[2]/div[3]/div[2]/div/a/div/span")
showmore_link.click()
sleep(random.randint(5,10))

# 5. Lấy tất cả thẻ div có aria-label = "Comment"
comment_list = browser.find_elements(By.XPATH, "//div[@aria-label='Comment']")
print(comment_list)

for comment in comment_list:
    # Hiển thị tên người dùng và nội dung, cách nhau bởi dấu :
    poster = comment.find_element(By.CLASS_NAME, "_6qw4")
    content = comment.find_element(By.CLASS_NAME, "_3l3x")
    print("*", poster.text, ":", content.text)

sleep(random.randint(5,10))

browser.close()
