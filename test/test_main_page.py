# -*- coding: utf-8 -*-
import allure


@allure.feature('Main page')
@allure.story('Validation')
@allure.title('Validation of page elements')
def test_main_page_elements(app):
    main_page = app.open_main_page()

    main_page.assert_element(main_page._MAIN_NAV_BAR)
    main_page.assert_element(main_page._SEARCH_FIELD)
    main_page.assert_element(main_page._MENU)
    main_page.assert_element(main_page._CART_BUTTON)
    main_page.assert_element(main_page._MAIN_SLIDER)
