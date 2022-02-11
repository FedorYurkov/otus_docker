# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from application.pages.base_page import BasePage


class MainPage(BasePage):
    _SEARCH_FIELD = (By.CSS_SELECTOR, "#search")
    _MENU = (By.CSS_SELECTOR, "#menu")
    _CART_BUTTON = (By.CSS_SELECTOR, "#cart")
    _MAIN_SLIDER = (By.CSS_SELECTOR, "#slideshow0")

    def __init__(self, app):
        super().__init__(app)
