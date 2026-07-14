import pytest
from playwright.sync_api import Page, expect

from conftest import page
from pages.login_page import loginPageClass
from pages.product_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from test_Data.credentials import CREDENTIALS
from test_Data.checkout_data import *

def test_checkout_flow(page: Page, login_page, products_page, cart_page, checkout_page):
    login_page.login(
        CREDENTIALS["standard"]["username"],
        CREDENTIALS["standard"]["password"]
    )
    products_page.add_product(products_page.Sauce_Labs_Backpack)
    products_page.click_on_the_cart()
    cart_page.click_on_the_checkout()
    checkout_page.Enter_Details_At_Checkout(
        CHECKOUT_DATA1["FirstName"],
        CHECKOUT_DATA1["LastName"],
        CHECKOUT_DATA1["ZipCode"]
    )
    checkout_page.Click_on_Finish_button()
    checkout_page.verify_order_successful_message()
    page.wait_for_timeout(2000)


    