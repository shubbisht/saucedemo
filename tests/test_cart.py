import pytest
from playwright.sync_api import Page, expect

from conftest import page
from pages.login_page import loginPageClass
from pages.product_page import ProductsPage
from test_Data.credentials import CREDENTIALS

def test_add_product_to_cart(page: Page, login_page, products_page):
    login_page.login(
        CREDENTIALS["standard"]["username"],
        CREDENTIALS["standard"]["password"]
    )
    products_page.add_product(products_page.Sauce_Labs_Backpack)
    products_page.add_product(products_page.Sauce_Labs_Bike_Light)

    products_page.verify_cart_count()
