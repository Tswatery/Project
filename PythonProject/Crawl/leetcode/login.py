import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
chrome = webdriver.Chrome(options=options)

chrome.get("https://leetcode.cn/accounts/login/?next=%2F")

wait = WebDriverWait(chrome, 5)
account_switch = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".css-1o8m92c-Item.e19orumq1")))
account_switch.click()

input_list = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ex750351.css-xpyj6f-BasicInputComponent-StyledBasicInput.en6ooyu0")))

account_username, account_password = input_list[0], input_list[1]
account_username.send_keys("18355693652")
account_password.send_keys("Tsinghua2024")

login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".e4jw0mn0.css-mo585l-BaseButtonComponent-StyledButton.ery7n2v0")))
login_button.click()
time.sleep(20)
# 登陆leetcode登陆不上去