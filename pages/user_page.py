from pages.base_page import BasePage
from pages.locators import UserPageLocators


class UserPage(BasePage):
    def go_to_edit_page(self):
        link = self.browser.find_element(*UserPageLocators.GO_TO_EDIT_BUTTON)
        link.click()

    def test_field_first_name(self):
        insert_email = self.browser.find_element(*UserPageLocators.FIELD_FIRST_NAME)
        insert_email.send_keys("Ivan56")
