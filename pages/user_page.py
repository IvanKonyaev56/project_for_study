from pages.base_page import BasePage
from pages.locators import UserPageLocators


class UserPage(BasePage):
    def go_to_edit_page(self):
        link = self.browser.find_element(*UserPageLocators.GO_TO_EDIT_BUTTON)
        link.click()

    def accept_cookie(self):
        find_the_button = self.browser.find_element(*UserPageLocators.COOKIE_SUBMIT_BUTTON)
        find_the_button.click()

    def click_to_button_tax_free_form(self):
        find_the_button = self.browser.find_element(*UserPageLocators.NEW_TAX_FREE_FORM_BUTTON)
        find_the_button.click()

    def fill_in_the_field_name(self):
        find_field_name = self.browser.find_element(*UserPageLocators.FIELD_FIRST_NAME)
        find_field_name.send_keys("Ivan")

    def fill_in_the_field_last_name(self):
        find_field_last_name = self.browser.find_element(*UserPageLocators.FIELD_LAST_NAME)
        find_field_last_name.send_keys("Ivanov")

    def fill_in_the_date_of_birth(self):
        find_calendar_icon = self.browser.find_element(*UserPageLocators.CALENDAR_ICON)
        find_calendar_icon.click()
        find_month = self.browser.find_element(*UserPageLocators.MONTH_BUTTON)
        find_month.click()
        find_arrow_previous = self.browser.find_element(*UserPageLocators.ARROW_PREVIOUS)
        find_arrow_previous.click()
        find_year = self.browser.find_element(*UserPageLocators.FIND_YEAR)
        find_year.click()
        find_month2 = self.browser.find_element(*UserPageLocators.FIND_MONTH)
        find_month2.click()
        find_day = self.browser.find_element(*UserPageLocators.FIND_DAY)
        find_day.click()

    def fill_in_the_country_of_issue(self):
        find_field_country = self.browser.find_element(*UserPageLocators.FIELD_COUNTRY)
        find_field_country.click()
        find_field_search = self.browser.find_element(*UserPageLocators.FIELD_SEARCH)
        find_field_search.send_keys("united")
        find_needed_country = self.browser.find_element(*UserPageLocators.NEEDED_COUNTRY)
        find_field_country.click()
