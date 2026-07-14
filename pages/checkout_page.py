from playwright.sync_api import Page, expect

class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page
        self.FirstNameTextField = page.locator("//input[@id='first-name']")
        self.LastNameTextField = page.locator("//input[@id='last-name']")
        self.ZipCodeTextField = page.locator("//input[@id='postal-code']")
        self.ContinueButton = page.locator("//input[@id='continue']")
        self.FinishButton = page.locator("//button[@id='finish']")
        self.successful_message = page.locator("//h2[@class='complete-header']")


    def Enter_Details_At_Checkout(self, FirstName, LastName, ZipCode):
        self.FirstNameTextField.fill(FirstName)
        self.LastNameTextField.fill(LastName)
        self.ZipCodeTextField.fill(ZipCode)
        self.ContinueButton.click()

    def Click_on_Finish_button(self):
        self.FinishButton.click()

    def verify_order_successful_message(self):
        expect(self.successful_message).to_have_text("Thank you for your order!")