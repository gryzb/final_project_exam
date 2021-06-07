from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_correct_success_message(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK).text == self.browser.find_element(*ProductPageLocators.NAME_OF_BOUGHT_BOOK).text , "Название товара совпадает"
        assert ("был добавлен в вашу корзину." in self.browser.find_element(*ProductPageLocators.TEXT_OF_SUCCESS_BUING).text), "Сообщение о добавлении в корзину отображается"

    def should_be_correct_price(self):
        assert self.browser.find_element(*ProductPageLocators.CURRENT_PRICE).text == self.browser.find_element(*ProductPageLocators.FINAL_PRICE).text, "Цена совпадает"
        assert ("Стоимость корзины теперь составляет" in self.browser.find_element(*ProductPageLocators.TEXT_OF_FINAL_PRICE).text), "Текст стоимости отображается"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE) == False, \
            "Success message is presented, but should not be"

    def should_not_be_success_message_disapear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
