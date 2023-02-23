from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def login_user(self, email, password):
        insert_email = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS)
        insert_email.send_keys(email)
        insert_password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        insert_password.send_keys(password)
        click_to_button_reg = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        click_to_button_reg.click()
