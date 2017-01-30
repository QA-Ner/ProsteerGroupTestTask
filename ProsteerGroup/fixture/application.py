__author__ = 'Nazar Ner'

from selenium import webdriver
from fixture.product import Product


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://gsmserver.com"
        self.product = Product(self)

    def destroy(self):
        self.driver.quit()

