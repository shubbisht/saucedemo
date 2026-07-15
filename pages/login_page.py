from playwright.sync_api import Page, expect
import pytest

class loginPageClass():
    def __init__(self, page: Page):
        self.page = page
        self.userNameTextField = page.get_by_placeholder("Username")
        self.passwordTextField = page.get_by_placeholder("Password")
        self.signInButton = page.get_by_role("button", name="Login")
        self.lockedErrorMessage = page.locator("//h3[@data-test='error']")

    def login(self, username, password):
        self.userNameTextField.fill(username)
        self.passwordTextField.fill(password)
        self.signInButton.click()

    def locked_verify_error_message(self):
        expect(self.lockedErrorMessage).to_have_text("Epic sadface: Sorry, this user has been locked out.")