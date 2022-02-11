# -*- coding: utf-8 -*-
import allure
from selenium.webdriver.common.by import By

from application.pages.base_page import BasePage


class AdminMainPage(BasePage):
    _CATALOG_MENU_ITEM = (By.CSS_SELECTOR, "#menu-catalog")
    _PRODUCTS_MENU_ITEM = (By.XPATH, "//a[.='Products']")

    def __init__(self, app):
        super().__init__(app)

    @allure.step("Open products page from admin panel menu")
    def open_admin_products_page(self):
        self.driver.find_element(*self._CATALOG_MENU_ITEM).click()
        self.driver.find_element(*self._PRODUCTS_MENU_ITEM).click()
