# -*- coding: utf-8 -*-
import allure
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _MAIN_NAV_BAR = (By.CSS_SELECTOR, "#top")
    _MAIN_NAV_BAR_CURRENCY = (By.CSS_SELECTOR, "#form-currency button[data-toggle='dropdown']")
    _CURRENCY_MENU_ITEM_EUR = (By.CSS_SELECTOR, "#form-currency button[name='EUR']")
    _CURRENCY_MENU_ITEM_GBP = (By.CSS_SELECTOR, "#form-currency button[name='GBP']")
    _CURRENCY_MENU_ITEM_USD = (By.CSS_SELECTOR, "#form-currency button[name='USD']")

    # General methods

    def __init__(self, app):
        self.driver = app.driver
        self.wait = WebDriverWait(self.driver, 15)

    def assert_element(self, locator, special_timeout=None):
        if special_timeout:
            wait = WebDriverWait(self.driver, special_timeout)
        else:
            wait = self.wait

        try:
            wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента: {locator}")

    def type(self, locator, value):
        field = self.driver.find_element(*locator)
        current_value_in_field = field.get_attribute("value")
        if current_value_in_field != value:
            field.click()
            if current_value_in_field != '':
                field.clear()
            field.send_keys(value)
        return self

    def is_displayed(self, locator, context=None):
        if not context:
            context = self.driver
        try:
            return context.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False

    # Methods of working with MAIN NAV BAR

    @allure.step("Switch currency to: {to}")
    def switch_currency_in_main_nav(self, to):
        if to == "EUR":
            locator = self._CURRENCY_MENU_ITEM_EUR
        elif to == "GBP":
            locator = self._CURRENCY_MENU_ITEM_GBP
        elif to == "USD":
            locator = self._CURRENCY_MENU_ITEM_USD
        else:
            raise RuntimeError("Unsupported currency!")

        self.driver.find_element(*self._MAIN_NAV_BAR_CURRENCY).click()
        self.driver.find_element(*locator).click()

        return self

    @allure.step("Get currency text")
    def get_currency_text_from_main_nav(self):
        return self.driver.find_element(*self._MAIN_NAV_BAR_CURRENCY).text
