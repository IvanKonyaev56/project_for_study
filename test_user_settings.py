import time
import pytest
from pages.user_page import UserPage
from pages.login_page import LoginPage


class TestUserSettingsPassport:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "https://taxfree-auth-service-demo.wavea.cc/en/login"
        page = LoginPage(browser, self.link)
        page.open()
        page.login_user("ivanwatester2@gmail.com", "marvel56")

    def test_guest_can_go_to_passport_page(self, browser):
        page = UserPage(browser, self.link)
        page.go_to_edit_page()
        page.test_field_first_name()
        time.sleep(5)
