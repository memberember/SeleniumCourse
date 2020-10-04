import unittest
from selenium import webdriver
import time

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля

        input1 = browser.find_element_by_css_selector('.first_class input:required')
        input1.send_keys("first")

        input2 = browser.find_element_by_css_selector('.second_class input:required')
        input2.send_keys("second")

        input3 = browser.find_element_by_css_selector('.third_class input:required')
        input3.send_keys("third")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!', "Ошибка ебаная")

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля

        input1 = browser.find_element_by_css_selector('.first_class input:required')
        input1.send_keys("first")

        input2 = browser.find_element_by_css_selector('.second_class input:required')
        input2.send_keys("second")

        input3 = browser.find_element_by_css_selector('.third_class input:required')
        input3.send_keys("third")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!', "Ошибка ебаная")



if __name__ == "__main__":
    unittest.main()