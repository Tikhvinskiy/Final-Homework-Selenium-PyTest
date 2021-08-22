from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def guest_add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        link.click()

    def check_product_name_and_adding(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), (
            "there is no product name")
        assert self.is_element_present(*ProductPageLocators.ADDING_PRODUCT), (
            "there is no adding message")
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        add_message = self.browser.find_element(*ProductPageLocators.ADDING_PRODUCT).text
        assert product_name == add_message, "there is no product name in the message"

    def check_message_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), (
            "there is no basket total")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
            "there is no product price")
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price == message_basket_total, "there is no product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"
