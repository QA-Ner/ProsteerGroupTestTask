__author__ = 'Nazar Ner'

import time

class Product:
    def __init__(self, app):
        self.app = app

    def proceed_to_checkout(self):
        # Proceed to Checkout
        driver = self.app.driver
        driver.find_element_by_id("goto-checkout").click()
        # Buy without registration
        driver.find_element_by_link_text("Buy without registration").click()
        # Go to Contact Information page
        driver.find_element_by_link_text("Next step").click()

    def assert_discount(self):
        driver = self.app.driver
        specialprice = driver.find_element_by_css_selector(".product-price.special-price")
        oldprice = driver.find_element_by_css_selector("span[data-old-price='']")
        assert specialprice.text < oldprice.text

    def go_to_cart_page(self):
        driver = self.app.driver
        driver.get(self.app.base_url + '/cart/')

    def set_quantity(self, quantity):
        driver = self.app.driver
        driver.find_element_by_name("quantity").clear()
        driver.find_element_by_name("quantity").send_keys(quantity)
        time.sleep(2)

    def add_to_cart(self):
        driver = self.app.driver
        driver.find_element_by_css_selector(".bottom>.product-button-wrapper>.add-to-cart>a").click()
        time.sleep(1)

    def find_by_cod(self, productcod):
        driver = self.app.driver
        driver.get(self.app.base_url + '/search/?f=all&q=' + productcod)

