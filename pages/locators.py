# import total as total
from selenium.webdriver.common.by import By


class BasePageLocators:
    pass


class LoginPageLocators:
    EMAIL_ADDRESS = (By.CSS_SELECTOR, "#username")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary.full-width.m-bottom-6")

class UserPageLocators:
    GO_TO_EDIT_BUTTON = (By.CSS_SELECTOR, ".user-edit-btn:nth-child(2)")
    FIELD_FIRST_NAME = (By.CSS_SELECTOR, "[formcontrolname='name']")
