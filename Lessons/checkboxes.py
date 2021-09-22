from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_css_selector('span[class ="nowrap"][id="input_value"]').text
    y = str(math.log(abs(12*math.sin(int(x)))))

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)

    input2 = browser.find_element_by_css_selector('input[class="form-check-input"][type="checkbox"]')
    input2.click()

    input3 = browser.find_element_by_css_selector('div[class="form-check form-radio-custom"] input[type="radio"]')
    input3.click()

    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()

    answer = browser.switch_to.alert.text
    print(answer.split()[-1])

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()