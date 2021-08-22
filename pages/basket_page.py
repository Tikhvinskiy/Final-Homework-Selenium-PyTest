from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_go_to_basket_page(self):
        button = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        button.click()

    def should_not_see_product_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.PRODUCT_IN_BASKET), \
            "Product in basket is presented, but should not be"

    def should_see_empty_basket(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET)