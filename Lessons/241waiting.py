from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math, time
from send_answer import send_answer

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
browser.implicitly_wait(5)
button = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h5[id="price"]'), '$100')
    )
if button:
    browser.find_element_by_css_selector('button[id="book"]').click()

    x = browser.find_element_by_css_selector('span[id="input_value"]').text
    y = str(math.log(abs(12 * math.sin(int(x)))))
    input1 = browser.find_element_by_css_selector('input[class="form-control"]')
    input1.send_keys(y)
    button = browser.find_element_by_css_selector('button[id="solve"]').click()
    answer = browser.switch_to.alert.text.split()[-1]
    print(answer)
    browser.quit()
    send_answer(answer, 'https://stepik.org/lesson/181384/step/8?unit=156009')


# Ситуация: тяжеловесный сайт через впн очень долго грузится, иногда бесконечно долго, соответственно код не
# выполняется, пока не остановишь загрузку. Но жать вручную на крестик - это отбирать хлеб у роботов. Гуглил, нашел
# решение в настройках pageLoadStrategy (по умолчанию 'normal', также принимает 'eager' или 'none'). Пример кода:
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
# link = "example.com"
# caps = DesiredCapabilities.CHROME
# browser = webdriver.Chrome(desired_capabilities=caps)
# caps["pageLoadStrategy"] = "none"
# browser.get(link)
# # ждем загрузку элемента:
# WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".example_selector")))
# # стопаем загрузку сайта:
# browser.execute_script("window.stop();")
