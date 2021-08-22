from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, 'a[class="btn btn-default"]')
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "h2.h3")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, 'form[id="login_form"]')
    REG_FORM = (By.CSS_SELECTOR, 'form[id="register_form"]')


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[class="btn btn-lg btn-primary btn-add-to-basket"]')
    ADDING_PRODUCT = (By.CSS_SELECTOR, 'div.alert-success:first-child  strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main h1')
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, '.alert-info :first-child :first-child')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")