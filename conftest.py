# -*- coding: utf-8 -*-
import allure
import pytest
from selenium import webdriver

from application.app import App


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="https://demo.opencart.com")
    parser.addoption("--executor", action="store", default="local")
    parser.addoption("--vnc", action="store_true", default=True)


def driver_factory(browser, executor, vnc):
    if executor == "local":
        if browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "firefox":
            driver = webdriver.Firefox()
        elif browser == "opera":
            driver = webdriver.Opera()
        else:
            raise Exception("Browser not supported")
    else:
        executor_url = f"http://{executor}:4444/wd/hub"
        caps = {
            "browserName": browser,
            "selenoid:options": {
                "enableVNC": vnc
            }
        }
        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )

    driver.maximize_window()
    return driver


@pytest.fixture
def app(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")

    driver = driver_factory(browser, executor, vnc)
    url = request.config.getoption("--url")

    application = App(driver=driver, base_url=url)

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return application


def pytest_exception_interact(node):
    if "app" in node.funcargs:
        allure.attach(
            body=node.funcargs["app"].driver.get_screenshot_as_png(),
            name="screenshot_image",
            attachment_type=allure.attachment_type.PNG
        )
