from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException  # в начале файла
from math import log, sin
import time

class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(log(abs((12 * sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
        # time.sleep(100)

    def get_product_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return price

    def get_product_title(self):
        title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)
        return title.text

    def get_title_product_title(self):
        title = self.browser.find_element(*ProductPageLocators.TITLE_PRODUCT_TITLE).text
        return title

    def get_title_product_price(self):
        price = self.browser.find_element(*ProductPageLocators.TITLE_PRODUCT_PRICE).text
        return price

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def is_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"
