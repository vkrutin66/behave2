from selenium.common.exceptions import NoSuchElementException

from locators.Locator import Locator
from log.Log import Log
from pages.Book import Book
from pages.Page import Page


class SearchResult(Page):

    items = Locator("CSS", ".s-result-item")

    def get_book_name_loc(self, i):
        return Locator("CSS", ".s-result-item:nth-child(" + str(i) + ") .a-section h5")

    def get_author_loc(self, i):
        return Locator("CSS", ".s-result-item:nth-child(" + str(i) + ") .a-color-secondary .a-link-normal")

    def get_stars_loc(self, i):
        return Locator("CSS", ".s-result-item:nth-child(" + str(i) + ") .a-icon-star-small span")

    def get_price_loc1(self, i):
        return Locator("CSS", ".s-result-item:nth-child(" + str(i) + ") .a-price-whole")

    def get_price_loc2(self, i):
        return Locator("CSS", ".s-result-item:nth-child(" + str(i) + ") .a-price-fraction")

    def get_element(self, locator):
        return self.browser.find_element(locator.get_by(), locator.get_name())

    def is_element_present(self, loc):
        try:
            self.browser.find_element(loc.get_by(), loc.get_name())
        except NoSuchElementException:
            return False
        return True

    def get_info(self):
        items = []
        for i in range(1, len(self.browser.find_elements(self.items.get_by(), self.items.get_name()))+1):
            book = Book()
            book.set_name(self.get_element(self.get_book_name_loc(i)).text)
            if self.is_element_present(self.get_author_loc(i)):
                book.set_author(self.get_element(self.get_author_loc(i)).text)
            if self.is_element_present(self.get_price_loc1(i)):
                price = float(self.get_element(self.get_price_loc1(i)).text)
                price += float(self.get_element(self.get_price_loc2(i)).text)/100
                book.set_price(price)
            if self.is_element_present(self.get_stars_loc(i)):
                stars = self.get_element(self.get_stars_loc(i)).get_attribute('innerHTML')[:3]
                if stars == '':
                    stars = '0.0'
                book.set_stars(float(stars))
            items.append(book)
            Log.log(book.get_name())
            Log.log(book.get_author())
            Log.log(str(book.get_price()))
            Log.log(str(book.get_stars()))
        return items
