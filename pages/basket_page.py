from pages.base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_be_success_message_basket(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_TEXT), \
            "Success message is presented"

    def should_not_be_success_message_basket(self):
        assert self.is_not_element_present(*BasePageLocators.EMPTY_BASKET_TEXT), "Success message is not presented"
