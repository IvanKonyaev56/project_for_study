import time
import pytest
from pages.user_page import UserPage
from pages.login_page import LoginPage


class TestPositivRegistraion:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "https://taxfree-auth-service-demo.wavea.cc/en/login"
        page = LoginPage(browser, self.link)
        page.open()
        page.login_user("eqonte@mailto.plus", "marvel56")

    # Gроверка заполнения полей на шаге "Паспортные данные".
    def test_first_step(self, browser):
        page = UserPage(browser, self.link)
        page.accept_cookie()
        page.click_to_button_tax_free_form()
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
        time.sleep(2)

    # Gроверка заполнения полей на шаге "Платёжные данные".
    # def test_second_step(self, browser):
    #     pass
