from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        input1 = self.browser.find_element(*LoginPageLocators.IN1)
        input1.send_keys(email)
        input2 = self.browser.find_element(*LoginPageLocators.IN2)
        input2.send_keys(password)
        input3 = self.browser.find_element(*LoginPageLocators.IN3)
        input3.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.IN4)
        button_register.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, 'Login link is not presented'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'There is no login form'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), 'There is no register form'
