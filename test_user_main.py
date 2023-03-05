import time
import pytest
from pages.user_page import UserPage
from pages.login_page import LoginPage


class TestPositiveRegistration:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "https://taxfree-auth-service-demo.wavea.cc/en/login"
        page = LoginPage(browser, self.link)
        page.open()
        page.login_user("tqyow@mailto.plus", "marvel56")

    def test_first_step(self, browser):
        # После того как закончу основные моменты, переделать функции, чтобы можно было передавать вносимые
        # ими данные непосредственно при их вызове.
        page = UserPage(browser, self.link)
        page.accept_cookie()
        page.click_to_button_tax_free_form()

        # Проверка заполнения полей на шаге "Паспортные данные".
        page.fill_in_the_field_name()
        page.fill_in_the_field_last_name()
        page.fill_in_the_field_middle_name()
        page.fill_in_the_date_of_birth()
        page.fill_in_the_country_of_issue()
        page.fill_in_the_passport_number()
        page.fill_in_the_date_of_issue()
        page.fill_in_the_date_of_validity()
        page.create_a_screenshot("1_Паспортные данные")
        page.click_to_continue_button()

        # Проверка заполнения полей на шаге "Платёжные данные".
        page.fill_in_the_bankcard_number()
        page.fill_in_the_date_of_card_validity()
        page.fill_in_the_card_holder_name()
        page.fill_in_the_checkbox()
        page.create_a_screenshot("2_Платёжные данные")
        page.click_to_continue_button()

        # Проверка заполнения полей на шаге "Контактные данные".
        page.fill_in_the_phone_numbers()
        page.fill_in_the_email_address()
        page.create_a_screenshot("3_Контактные данные")
        time.sleep(5)
        page.click_to_continue_button()
