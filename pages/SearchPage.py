from locators.Locator import Locator
from pages.Page import Page


class SearchPage(Page):

    search_input = Locator("ID", "twotabsearchtextbox")

    def get_element(self, locator):
        return self.browser.find_element(locator.get_by(), locator.get_name())

    def search(self, search_value):
        self.get_element(self.search_input).send_keys(search_value)
        self.get_element(self.search_input).submit()
