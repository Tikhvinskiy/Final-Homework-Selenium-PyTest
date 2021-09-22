from selenium import webdriver
import time
import math


# link = "http://suninjuly.github.io/simple_form_find_task.html"

link = "http://suninjuly.github.io/find_xpath_form"
# url_math = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # link = browser.find_element_by_partial_link_text(url_math)
    # link.click()

    input1 = browser.find_element_by_tag_name("input.form-control")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_elements_by_xpath("//button[@type='submit']")
    # button = browser.find_element_by_xpath('//button[@type="submit"]')
    print(button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла