# -*- coding: utf-8 -*-
from time import time

import allure
import pytest

from application.pages.admin_main_page import AdminMainPage
from application.pages.admin_products_page import AdminProductsPage


@allure.feature('Admin panel')
@allure.story('Products')
@allure.title('Add product')
def test_add_new_product_from_admin(app):
    admin_user = {"login": "user", "password": "bitnami"}
    uniq = int(time())
    product = {"name": f"PRODUCT_{uniq}", "tag": f"TAG_{uniq}", "model": f"MODEL_{uniq}"}

    admin_auth_page = app.open_admin_page()
    admin_auth_page.login(admin_user["login"], admin_user["password"])

    AdminMainPage(app).open_admin_products_page()

    admin_products_page = AdminProductsPage(app)

    admin_products_page.init_product_add() \
        .fill_product_name(product["name"]) \
        .fill_product_meta_tag(product["tag"]) \
        .open_data_tab() \
        .fill_product_model(product["model"]) \
        .save_product()

    assert admin_products_page.is_product_in_list(product["name"])


@allure.feature('Admin panel')
@allure.story('Products')
@allure.title('Delete product')
def test_remove_product_from_admin(app):
    admin_user = {"login": "user", "password": "bitnami"}
    admin_auth_page = app.open_admin_page()
    admin_auth_page.login(admin_user["login"], admin_user["password"])

    AdminMainPage(app).open_admin_products_page()
    admin_products_page = AdminProductsPage(app)
    products_before = admin_products_page.get_products_rows()
    admin_products_page.mark_product_checked(products_before[-1]) \
        .click_product_delete_button() \
        .confirm_product_delete()

    products_after = admin_products_page.get_products_rows()
    assert len(products_after) == len(products_before) - 1


@allure.feature('User auth page')
@allure.story('Registration')
@allure.title('Correct user registration')
def test_user_registration(app):
    user_auth_page = app.open_user_auth_page()
    uniq = int(time())
    user_auth_page.fill_first_name(f"name_{uniq}") \
        .fill_last_name(f"surname_{uniq}") \
        .fill_email(f"{uniq}@test.com") \
        .fill_phone(f"+1{uniq}") \
        .fill_password("qwerty") \
        .fill_password_confirm("qwerty") \
        .fill_agree_with_privacy_checkbox() \
        .submit_continue_button()

    assert user_auth_page.driver.current_url == app.base_url + "/index.php?route=account/success"
    assert user_auth_page.get_content_title_text() == "Your Account Has Been Created!"


@allure.feature('Main page')
@allure.story('Validation')
@allure.title('Currency switcher')
@pytest.mark.parametrize("currency, currency_label", [("EUR", "€"), ("GBP", "£"), ("USD", "$")])
def test_switch_currency_from_main_nav(app, currency, currency_label):
    main_page = app.open_main_page()
    main_page.switch_currency_in_main_nav(to=currency)
    currency_text = main_page.get_currency_text_from_main_nav()
    assert currency_text == f"{currency_label} Currency "
