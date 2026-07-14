import pytest
from playwright.sync_api import Page, expect

from conftest import page
from pages.login_page import loginPageClass
from pages.product_page import ProductsPage
from test_Data.credentials import CREDENTIALS

def test_sort_products(page: Page, login_page, products_page):
    login_page.login(
        CREDENTIALS["standard"]["username"],
        CREDENTIALS["standard"]["password"]
    )
    products_page.sort_product_low_to_high()
    products_page.verifing_price_sorted_low_to_high()
