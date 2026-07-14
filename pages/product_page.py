from playwright.sync_api import Page, expect

class ProductsPage:

    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator("//span[@class='title']")
        self.Sauce_Labs_Backpack = "//button[@id='add-to-cart-sauce-labs-backpack']"
        self.Sauce_Labs_Bike_Light = "//button[@id='add-to-cart-sauce-labs-bike-light']"
        self.items_in_cart = page.locator("//a[@data-test='shopping-cart-link']")
        self.sort_dropdown = page.locator("//select[@class='product_sort_container']")
        self.product_prices = page.locator("//div[@class='inventory_item_price']")

    def verify_products_page(self):
        expect(self.title).to_have_text("Products")

    def add_product(self, product_locator):
        self.page.locator(product_locator).click()

    def verify_cart_count(self):
        expect(self.items_in_cart).to_have_text("2")

    def click_on_the_cart(self):
        self.items_in_cart.click()

    def sort_product_low_to_high(self):
        self.sort_dropdown.select_option("lohi")

    def verifing_price_sorted_low_to_high(self):
        prices = []
        all_prices = self.product_prices.all_text_contents()
        for price in all_prices:
            prices.append(float(price.replace("$", "")))
        assert prices == sorted(prices)
        
    
