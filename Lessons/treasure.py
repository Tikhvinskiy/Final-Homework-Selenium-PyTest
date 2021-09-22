from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_css_selector('img[id="treasure"]').get_attribute("valuex")
    y = str(math.log(abs(12 * math.sin(int(x)))))

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)

    input2 = browser.find_element_by_css_selector('input[class="check-input"][type="checkbox"]')
    input2.click()

    input3 = browser.find_element_by_css_selector('input[class="check-input"][type="radio"][value="robots"]')
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
