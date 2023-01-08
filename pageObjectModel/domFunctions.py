import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DomHelper(object):
    def __init__(self, driver):
        self.driver = driver

    ##Open Page##
    def open_Page(self, url):
        self.driver.get(url)
    ##DriverQuit##
    def driver_Quit(self):
        self.driver.quit()
    ##ClickButton##
    def click_button_ID(self, selector):
        click_Function=self.driver.find_element(By.ID, selector)
        click_Function.click()
        # print(click_Function.text)
    def click_button_XPATH(self, selector):
        click_Function=self.driver.find_element(By.XPATH, selector)
        click_Function.click()
        # print(click_Function.text)
    def click_button_CSS_SELECTOR(self, selector):
        click_Function=self.driver.find_element(By.CSS_SELECTOR, selector)
        click_Function.click()
        # print(click_Function.text)
    def click_button_CSS_NAME(self, selector):
        click_Function = self.driver.find_element(By.CLASS_NAME, selector)
        click_Function.click()
        # print(click_Function.text)
    ##SendKeys##
    def send_keys_ID(self, selector, text):
        text_field = self.driver.find_element(By.ID, selector)
        text_field.clear()
        text_field.send_keys(text)

    def send_keys_XPATH(self, selector, text):
        text_field = self.driver.find_element(By.XPATH, selector)
        text_field.clear()
        text_field.send_keys(text)
    def send_keys_CSS_SELECTOR(self, selector, text):
        text_field = self.driver.find_element(By.CSS_SELECTOR, selector)
        text_field.clear()
        text_field.send_keys(text)
    def send_keys_CSS_NAME(self, selector, text):
        text_field = self.driver.find_element(By.CLASS_NAME, selector)
        text_field.clear()
        text_field.send_keys(text)

    ##TestEquals##
    def is_text_equal_ID(self, selector, text):
        text_equal=self.driver.find_element(By.ID, selector)
        assert text_equal.text in text
        print(text_equal.text)
    def is_text_equal_XPATH(self, selector, text):
        text_equal=self.driver.find_element(By.XPATH, selector)
        assert text_equal.text in text
        print(text_equal.text)
    def is_text_equal_CSS_SELECTOR(self, selector, text):
        text_equal=self.driver.find_element(By.CSS_SELECTOR, selector)
        assert text_equal.text in text
        print(text_equal.text)
    def is_text_equal_CSS_NAME(self, selector, text):
        text_equal=self.driver.find_element(By.CLASS_NAME, selector)
        assert text_equal.text in text
        print(text_equal.text)
    ##TextSplitEquals##
    def is_text_equal_XPATH_split_A(self, selector, text):
        text_equal = self.driver.find_element(By.XPATH, selector)
        assert text_equal.text.split()[1] in text
        print(text_equal.text)
    def is_text_equal_XPATH_split_B(self, selector, text):
        text_equal = self.driver.find_element(By.XPATH, selector)
        assert text_equal.text.split()[0], text_equal.text.split()[1] in text
        print(text_equal.text.split()[0], text_equal.text.split()[1])
    def is_text_equal_XPATH_split_C(self, selector, text):
        text_equal = self.driver.find_element(By.XPATH, selector)
        assert text_equal.text.split()[2], text_equal.text.split()[3] in text
        print(text_equal.text.split()[2], text_equal.text.split()[3])
     ##Displayed##
    def is_displayed_ID(self, selector):
        displayed = self.driver.find_element(By.ID, selector)
        assert displayed.is_displayed()
        print(displayed.text)
    def is_displayed_XPATH(self, selector):
        displayed = self.driver.find_element(By.XPATH, selector)
        assert displayed.is_displayed()
        print(displayed.text)
    def is_displayed_CSS_SELECTOR(self, selector):
        displayed = self.driver.find_element(By.CSS_SELECTOR, selector)
        assert displayed.is_displayed()
        print(displayed.text)
    def is_displayed_CSS_NAME(self, selector):
        displayed = self.driver.find_element(By.CLASS_NAME, selector)
        assert displayed.is_displayed()
        print(displayed.text)
    ##Selected##
    def is_selected_ID(self, selector):
            selected = self.driver.find_element(By.ID, selector)
            assert selected.is_selected()
            print(selected.text)
    def is_selected_XPATH(self, selector):
            selected = self.driver.find_element(By.XPATH, selector)
            assert selected.is_selected()
            print(selected.text)
    def is_selected_CSS_SELECTOR(self, selector):
            selected = self.driver.find_element(By.CSS_SELECTOR, selector)
            assert selected.is_selected()
            print(selected.text)
    def is_selected_CSS_NAME(self, selector):
            selected = self.driver.find_element(By.CLASS_NAME, selector)
            assert selected.is_selected()
            print(selected.text)