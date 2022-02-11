# -*- coding: utf-8 -*-

import allure


@allure.feature('Catalog page')
@allure.story('Validation')
@allure.title('Validation of page elements')
def test_catalog_page_elements(app):
    catalog_page = app.open_catalog_page()

    catalog_page.assert_element(catalog_page._BREADCRUMB)
    catalog_page.assert_element(catalog_page._CATEGORY_TITLE)
    catalog_page.assert_element(catalog_page._LIST_VIEW_BUTTON)
    catalog_page.assert_element(catalog_page._GRID_VIEW_BUTTON)
    catalog_page.assert_element(catalog_page._SORT_FIELD)
