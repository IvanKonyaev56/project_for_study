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
    FIELD_MIDDLE_NAME = (By.CSS_SELECTOR, "[formcontrolname='patronymic']")

    CALENDAR_ICON_1 = (By.CSS_SELECTOR,
                       "div:nth-child(1) > div > div:nth-child(4) > div > div > mat-datepicker-toggle > button")
    MONTH_BUTTON = (By.CSS_SELECTOR, "[id = mat-calendar-button-0]")
    ARROW_PREVIOUS = (By.CSS_SELECTOR,
                      ".mat-focus-indicator.mat-calendar-previous-button.mat-icon-button.mat-button-base")
    FIND_YEAR = (By.XPATH, "//div[text()=' 2000 ']")
    FIND_MONTH = (By.XPATH, "//div[text()=' JAN ']")
    FIND_DAY = (By.XPATH, "//div[text()=' 1 ']")

    FIELD_COUNTRY = (By.CSS_SELECTOR, "[placeholder='No country selected']")
    FIELD_SEARCH = (By.CSS_SELECTOR, ".form-control.searchable")
    NEEDED_COUNTRY = (By.XPATH, "//span[text()='United Kingdom']")
    PASSPORT_NUMBER = (By.CSS_SELECTOR, "[formcontrolname='number']")

    CALENDAR_ICON_2 = (By.CSS_SELECTOR,
                       "div:nth-child(2) > div > div:nth-child(3) > div > div > mat-datepicker-toggle > button")
    MONTH_BUTTON_2 = (By.CSS_SELECTOR, "[id = mat-calendar-button-1]")
    FIND_YEAR_2 = (By.XPATH, "//div[text()=' 2020 ']")
    FIND_MONTH_2 = (By.XPATH, "//div[text()=' JAN ']")
    FIND_DAY_2 = (By.XPATH, "//div[text()=' 1 ']")

    CALENDAR_ICON_3 = (By.CSS_SELECTOR,
                       "div:nth-child(2) > div > div:nth-child(4) > div > div > mat-datepicker-toggle > button")
    MONTH_BUTTON_3 = (By.CSS_SELECTOR, "[id = mat-calendar-button-2]")
    ARROW_FUTURE = (By.CSS_SELECTOR, ".mat-focus-indicator.mat-calendar-next-button.mat-icon-button.mat-button-base")
    FIND_YEAR_3 = (By.XPATH, "//div[text()=' 2050 ']")
    FIND_MONTH_3 = (By.XPATH, "//div[text()=' JAN ']")
    FIND_DAY_3 = (By.XPATH, "//div[text()=' 1 ']")

    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".btn-holder .btn.btn-primary")
