# -*- coding: utf-8 -*-
import allure
from selenium.webdriver.common.by import By

from application.pages.base_page import BasePage


class AdminProductsPage(BasePage):
    _ADD_NEW_BUTTON = (By.CSS_SELECTOR, "a[data-original-title='Add New']")
    _DELETE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Delete']")

    _PRODUCT_NAME_FIELD = (By.CSS_SELECTOR, "#input-name1")
    _PRODUCT_TAG_FIELD = (By.CSS_SELECTOR, "#input-meta-title1")
    _DATA_TAB_LABEL = (By.CSS_SELECTOR, "a[href='#tab-data']")
    _PRODUCT_MODEL = (By.CSS_SELECTOR, "#input-model")
    _SAVE_PRODUCT_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Save']")

    _PRODUCT_ROW_IN_PRODUCTS_TABLE = (By.CSS_SELECTOR, "#form-product tbody tr")
    _CHECKBOX_IN_RODUCT_ROW = (By.CSS_SELECTOR, "input[type='checkbox']")

    def __init__(self, app):
        super().__init__(app)

    @allure.step("Click ADD button")
    def init_product_add(self):
        self.driver.find_element(*self._ADD_NEW_BUTTON).click()
        return self

    @allure.step("Type product name: {product_name}")
    def fill_product_name(self, product_name):
        self.type(self._PRODUCT_NAME_FIELD, product_name)
        return self

    @allure.step("Type product tag: {product_tag}")
    def fill_product_meta_tag(self, product_tag):
        self.type(self._PRODUCT_TAG_FIELD, product_tag)
        return self

    @allure.step("Open data tab on product")
    def open_data_tab(self):
        self.driver.find_element(*self._DATA_TAB_LABEL).click()
        return self

    @allure.step("Type product model: {product_model}")
    def fill_product_model(self, product_model):
        self.type(self._PRODUCT_MODEL, product_model)
        return self

    @allure.step("Click SAVE button")
    def save_product(self):
        self.driver.find_element(*self._SAVE_PRODUCT_BUTTON).click()
        return self

    @allure.step("Verify is product with name '{product_name}' in list")
    def is_product_in_list(self, product_name):
        locator = (By.XPATH, f"//td[.='{product_name}']")
        return self.is_displayed(locator)

    @allure.step("Get products rows add elements")
    def get_products_rows(self):
        return self.driver.find_elements(*self._PRODUCT_ROW_IN_PRODUCTS_TABLE)

    @allure.step("Click checkbox on product")
    def mark_product_checked(self, product_row):
        product_row.find_element(*self._CHECKBOX_IN_RODUCT_ROW).click()
        return self

    @allure.step("Click Delete button")
    def click_product_delete_button(self):
        self.driver.find_element(*self._DELETE_BUTTON).click()
        return self

    @allure.step("Confirm alert")
    def confirm_product_delete(self):
        self.driver.switch_to.alert.accept()
        return self
