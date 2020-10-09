from .base_page import BasePage
from .locators import *
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert str(self.browser.current_url).find('login'), "Login link is not presented2"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_LINK), "Login link is not presented1"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL)
        password1 = self.browser.find_element(*LoginPageLocators.PASSWORD1)
        password2 = self.browser.find_element(*LoginPageLocators.PASSWORD2)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        email_field.send_keys(email)
        password1.send_keys(password)
        password2.send_keys(password)
        register_button.click()

    def is_user_success_login(self):
        assert self.browser.find_element(*LoginPageLocators.SUCCESS_LOGIN), 'Пользователь на авторизовался'
