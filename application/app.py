# -*- coding: utf-8 -*-
import allure

from application.pages.admin_auth_page import AdminPage
from application.pages.catalog_page import CatalogPage
from application.pages.main_page import MainPage
from application.pages.product_page import ProductPage
from application.pages.user_auth_page import UserAuthPage


class App:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.implicitly_wait(3)
        self.base_url = base_url

        self.main_page = None
        self.catalog_page = None
        self.product_page = None
        self.admin_page = None
        self.user_auth_page = None

    @allure.step("Open main page")
    def open_main_page(self):
        self.driver.get(self.base_url)
        if not self.main_page:
            self.main_page = MainPage(self)
        return self.main_page

    @allure.step("Open catalog page. Category {category_id}")
    def open_catalog_page(self, category_id=20):
        self.driver.get(self.base_url + f"/index.php?route=product/category&path={category_id}")
        if not self.catalog_page:
            self.catalog_page = CatalogPage(self)
            self.catalog_page.category_id = category_id
        return self.catalog_page

    @allure.step("Open product page. Product {product_id}")
    def open_product_page(self, product_id=43):
        self.driver.get(self.base_url + f"/index.php?route=product/product&product_id={product_id}")
        if not self.product_page:
            self.product_page = ProductPage(self)
            self.product_page.product_id = product_id
        return self.product_page

    @allure.step("Open admin page")
    def open_admin_page(self):
        self.driver.get(self.base_url + "/admin/")
        if not self.admin_page:
            self.admin_page = AdminPage(self)
        return self.admin_page

    @allure.step("Open user_auth page")
    def open_user_auth_page(self):
        self.driver.get(self.base_url + "/index.php?route=account/register")
        if not self.user_auth_page:
            self.user_auth_page = UserAuthPage(self)
        return self.user_auth_page
