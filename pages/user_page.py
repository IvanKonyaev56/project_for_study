from pages.base_page import BasePage
from pages.locators import UserPageLocators
import time


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

    def fill_in_the_field_middle_name(self):
        find_field_middle_name = self.browser.find_element(*UserPageLocators.FIELD_MIDDLE_NAME)
        find_field_middle_name.send_keys("Ivanovich")

    def fill_in_the_date_of_birth(self):
        find_calendar_icon = self.browser.find_element(*UserPageLocators.CALENDAR_ICON_1)
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
        time.sleep(0.25)
        find_needed_country = self.browser.find_element(*UserPageLocators.NEEDED_COUNTRY)
        find_needed_country.click()

    def fill_in_the_passport_number(self):
        find_field_passport_number = self.browser.find_element(*UserPageLocators.PASSPORT_NUMBER)
        find_field_passport_number.send_keys("AA11BB")

    def fill_in_the_date_of_issue(self):
        find_calendar_icon = self.browser.find_element(*UserPageLocators.CALENDAR_ICON_2)
        find_calendar_icon.click()
        find_month = self.browser.find_element(*UserPageLocators.MONTH_BUTTON_2)
        find_month.click()
        find_year = self.browser.find_element(*UserPageLocators.FIND_YEAR_2)
        find_year.click()
        find_month2 = self.browser.find_element(*UserPageLocators.FIND_MONTH_2)
        find_month2.click()
        find_day = self.browser.find_element(*UserPageLocators.FIND_DAY_2)
        find_day.click()

    def fill_in_the_date_of_validity(self):
        find_calendar_icon = self.browser.find_element(*UserPageLocators.CALENDAR_ICON_3)
        find_calendar_icon.click()
        find_month = self.browser.find_element(*UserPageLocators.MONTH_BUTTON_3)
        find_month.click()
        find_arrow_future = self.browser.find_element(*UserPageLocators.ARROW_FUTURE)
        find_arrow_future.click()
        find_year = self.browser.find_element(*UserPageLocators.FIND_YEAR_3)
        find_year.click()
        find_month2 = self.browser.find_element(*UserPageLocators.FIND_MONTH_3)
        find_month2.click()
        find_day = self.browser.find_element(*UserPageLocators.FIND_DAY_3)
        find_day.click()

    def click_to_continue_button(self):
        find_button = self.browser.find_element(*UserPageLocators.CONTINUE_BUTTON)
        find_button.click()

    def fill_in_the_bankcard_number(self):
        find_field_bankcard_number = self.browser.find_element(*UserPageLocators.BANKCARD_NUMBER)
        find_field_bankcard_number.send_keys("4000 1111 2222 3333")
        time.sleep(1.25)

    def fill_in_the_date_of_card_validity(self):
        find_the_card_validity = self.browser.find_element(*UserPageLocators.CARD_VALIDITY)
        find_the_card_validity.click()
        find_year = self.browser.find_element(*UserPageLocators.FIND_YEAR_4)
        find_year.click()
        find_month = self.browser.find_element(*UserPageLocators.FIND_MONTH_4)
        find_month.click()

    def fill_in_the_card_holder_name(self):
        find_field_card_holder_name = self.browser.find_element(*UserPageLocators.CARD_HOLDER_NAME)
        find_field_card_holder_name.send_keys("Ivan Ivanov")

    def fill_in_the_checkbox(self):
        find_the_checkbox = self.browser.find_element(*UserPageLocators.CHECKBOX_LABEL)
        find_the_checkbox.click()
