import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://zerotrac.github.io/leetcode_problem_rating/#/")
time.sleep(5)
wait = WebDriverWait(driver, 5)
cnt = 1
file = open("problem.md", "w")
while 1:
    elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".el-input__inner")))
    start, end = elements[2], elements[3]
    if not start.get_attribute("value"):
        start.send_keys("1800")
    if not end.get_attribute("value"):
        end.send_keys("2000")
        time.sleep(1)
        end.send_keys(Keys.RETURN)
        time.sleep(1)

    problems = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".el-table__row")))
    file.write(f'现在是第{cnt}页的题目数据\n')
    for problem in problems:
        num = 1
        info = problem.find_elements(By.TAG_NAME, "td")
        title = info[1].find_element(By.CSS_SELECTOR, ".el-link__inner").text
        link = info[1].find_element(By.TAG_NAME, "a").get_attribute("href")
        score = info[4].text
        contest = info[2].find_element(By.TAG_NAME, "span").text
        s = f'{num}. 题目链接是[{title}]({link}), 来自于{contest}, \t它对应的分数是{score}\n'
        num += 1
        file.write(s)
    file.write('-'*40 + f'第{cnt}页结束' + '-' * 40 + '\n\n')
    cnt += 1
    next_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-next")))
    next_button.click()
    time.sleep(1)
    time.sleep(1)
    if cnt > 14: break
