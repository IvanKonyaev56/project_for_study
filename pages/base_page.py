from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(By.CSS_SELECTOR, what)
        except (NoSuchElementException):
            return False
        return True

    def create_a_screenshot(self, name_of_file):
        time.sleep(1)
        self.browser.save_screenshot("C:/Users/IvanHome/Desktop/{}.jpeg".format(name_of_file))
