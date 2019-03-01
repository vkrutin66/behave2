from selenium import webdriver

from log.Log import Log
from pages.SearchPage import SearchPage
from pages.SearchResult import SearchResult


class Action:

    def __init__(self, browser):
        if browser == "Firefox":
            self.browser = webdriver.Firefox(executable_path=r'drivers/geckodriver.exe')
        else:
            self.browser = webdriver.Chrome('drivers/chromedriver.exe')
        self.browser.maximize_window()
        Log.log("reset")

    def open_page(self, url):
        self.browser.get(url)
        Log.log("Open page " + url)

    def search(self, search_value):
        Log.log("Search: " + search_value)
        search_page = SearchPage(self.browser)
        search_page.search(search_value)

    def get_info(self):
        search_result = SearchResult(self.browser)
        return search_result.get_info()

    def is_word_in_arr(self, arr, word):
        for item in arr:
            if word in item.get_name():
                Log.log(word + " is in " + item.get_name())
            else:
                Log.log(word + " is not in " + item.get_name())

    def exit(self):
        Log.log("Quit")
        self.browser.quit()
