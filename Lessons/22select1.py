from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math, time
from send_answer import send_answer

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"

try:
    browser.get(link)
    time.sleep(2)
    x1 = browser.find_element_by_css_selector("#num1").text
    x2 = browser.find_element_by_css_selector("#num2").text
    x3 = int(x1) + int(x2)
    select = Select(browser.find_element_by_css_selector("#dropdown"))
    select.select_by_visible_text(str(x3))
    button = browser.find_element_by_css_selector('button[class="btn btn-default"]').click()

finally:
    answer = browser.switch_to.alert.text.split()[-1]
    print(answer)
    send_answer(answer, 'https://stepik.org/lesson/228249/step/3?unit=200781')
    time.sleep(5)
    browser.quit()




