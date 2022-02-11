# -*- coding: utf-8 -*-
import allure


@allure.feature('User auth page')
@allure.story('Validation')
@allure.title('Validation of page elements')
def test_user_auth_page_elements(app):
    user_auth_page = app.open_user_auth_page()

    user_auth_page.assert_element(user_auth_page._MAIN_NAV_BAR)
    user_auth_page.assert_element(user_auth_page._CONTENT_TITLE)
    user_auth_page.assert_element(user_auth_page._LOGIN_LINK_IN_FORM)
    user_auth_page.assert_element(user_auth_page._PERSONAL_DETAILS_SECTION)
    user_auth_page.assert_element(user_auth_page._AGREE_CHECKBOX)
