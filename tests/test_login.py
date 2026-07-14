import pytest
from playwright.sync_api import Page, expect

from conftest import page
from pages.login_page import loginPageClass
from pages.product_page import ProductsPage
from test_Data.credentials import CREDENTIALS

def test_standard_user(page: Page, login_page, products_page):
    login_page.login(
        CREDENTIALS["standard"]["username"],
        CREDENTIALS["standard"]["password"]
    )
    products_page.verify_products_page()

def test_locked_user(page: Page, login_page, products_page):
    login_page.login(
        CREDENTIALS["locked"]["username"],
        CREDENTIALS["locked"]["password"]
    )
    login_page.locked_verify_error_message()
