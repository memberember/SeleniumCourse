from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def is_basket_empty(self):
        print(self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE))
        assert self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE), 'Корзина не пуста'
