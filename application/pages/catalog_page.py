# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from application.pages.base_page import BasePage


class CatalogPage(BasePage):
    _BREADCRUMB = (By.CSS_SELECTOR, "ul.breadcrumb")
    _CATEGORY_TITLE = (By.CSS_SELECTOR, "#content h2")
    _LIST_VIEW_BUTTON = (By.CSS_SELECTOR, "#list-view")
    _GRID_VIEW_BUTTON = (By.CSS_SELECTOR, "#grid-view")
    _SORT_FIELD = (By.CSS_SELECTOR, "#input-sort")

    def __init__(self, app):
        super().__init__(app)
