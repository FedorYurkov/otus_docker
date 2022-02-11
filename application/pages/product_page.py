# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from application.pages.base_page import BasePage


class ProductPage(BasePage):
    _PRODUCT_TITLE = (By.CSS_SELECTOR, "#content h1")
    _ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#button-cart")
    _PHOTOS = (By.CSS_SELECTOR, "ul.thumbnails")
    _PRODUCT_NAV_BAR = (By.CSS_SELECTOR, "ul.nav-tabs")
    _RATING_BLOCK = (By.CSS_SELECTOR, ".rating")

    def __init__(self, app):
        super().__init__(app)
