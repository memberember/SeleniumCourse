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