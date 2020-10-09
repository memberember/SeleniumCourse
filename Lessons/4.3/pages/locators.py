from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_TITLE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    PRODUCT_PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    TITLE_PRODUCT_TITLE = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    TITLE_PRODUCT_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'alertinner')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISTRATION_LINK = (By.NAME, "registration-redirect_url")
    EMAIL = (By.NAME, 'registration-email')
    PASSWORD1 = (By.NAME, 'registration-password1')
    PASSWORD2 = (By.NAME, 'registration-password2')
    REGISTER_BUTTON = (By.NAME, 'registration_submit')
    SUCCESS_LOGIN = (By.XPATH, '//*[@id="messages"]/div[1]/div')


class BasketPageLocators():
    EMPTY_MESSAGE = (By.XPATH, '//*[@id="content_inner"]/p')
