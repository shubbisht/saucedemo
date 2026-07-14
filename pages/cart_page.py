from playwright.sync_api import Page, expect
import pytest

class CartPage():
    def __init__(self, page: Page):
        self.page = page
        self.checkoutButton = page.locator("//button[@id='checkout']")

    def click_on_the_checkout(self):
        self.checkoutButton.click()
        