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
    COOKIE_SUBMIT_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary.submit")
    NEW_TAX_FREE_FORM_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary.m-top-24")

    # Селекторы полей на шаге "Паспортные данные".
    FIELD_FIRST_NAME = (By.CSS_SELECTOR, "[formcontrolname='name']")
    FIELD_LAST_NAME = (By.CSS_SELECTOR, "[formcontrolname='surname']")
    CALENDAR_ICON = (By.CSS_SELECTOR, ".mat-focus-indicator.mat-icon-button.mat-button-base")
    MONTH_BUTTON = (By.CSS_SELECTOR, "[id = mat-calendar-button-0]")
    ARROW_PREVIOUS = (By.CSS_SELECTOR, ".mat-focus-indicator.mat-calendar-previous-button.mat-icon-button.mat-button-base")
    FIND_YEAR = (By.XPATH, "//div[text()=' 2000 ']")
    FIND_MONTH = (By.XPATH, "//div[text()=' JAN ']")
    FIND_DAY = (By.XPATH, "//div[text()=' 1 ']")
    FIELD_COUNTRY = (By.CSS_SELECTOR, ".ng-select.ng-select-single.ng-pristine.ng-invalid.ng-touched.ng-select-opened.ng-select-bottom")
    FIELD_SEARCH = (By.CSS_SELECTOR, ".form-control.searchable")
    NEEDED_COUNTRY = (By.XPATH, "//span[text()='United Kingdom']")


