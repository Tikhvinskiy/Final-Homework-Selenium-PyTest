from selenium import webdriver
import time, random

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        A = random.sample(list("AVHHTCVRESEWTYUJOLKLJ"), 1)
        B = random.sample(list("aaaaaqwrtooooooyuiooopsdfghjuuuuklzxcvbeeeeeeeenm"), random.randint(5, 30))
        C = ''.join(A + B).replace("u", ' ')
        element.send_keys(C)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()