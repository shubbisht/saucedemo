import pytest
from playwright.sync_api import Page, sync_playwright
from test_Data.api_data import api_testing_URL, api_key

from pages.login_page import loginPageClass
from pages.product_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture()
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()

        page.goto("https://www.saucedemo.com/")

        yield page
        browser.close()

@pytest.fixture()
def login_page(page):
    return loginPageClass(page)

@pytest.fixture()
def products_page(page):
    return ProductsPage(page)

@pytest.fixture()
def cart_page(page):
    return CartPage(page)

@pytest.fixture()
def checkout_page(page):
    return CheckoutPage(page)

@pytest.fixture()
def api_base_url():
    return api_testing_URL

@pytest.fixture()
def api_headers():
    return {"x-api-key": api_key}

@pytest.fixture(scope="session")
def api_request():
    with sync_playwright() as p:
        request_context = p.request.new_context()
        yield request_context
        request_context.dispose()
