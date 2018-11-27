from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BrowserKeywords():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\petra.zabojnikova\Documents\myProjects\study\TestLadies\chromedriver_win32\chromedriver.exe')

    def open_browser(self, url):
        """Opens a new browser instance to the given 'url'."""
        try:
            self.driver.get(url)
        except WebDriverException:
            raise WebDriverException('Opened browser with session id {0} failed.'.format(self.driver.session_id))
        return self.driver
    
    def switch_window(self, window_name):
        """Switches between active browser windows using 'index'"""
        try:
            self.driver.switch_to_window(window_name)
        except RuntimeError:
            raise RuntimeError("No window with window name {0} found".format(window_name))

    def close_browser(self):
        """Closes the current browser."""
        self.driver.close()

class ElementsKeywords():
    def __init__(self, driver):
        self.driver = driver
    
    def page_should_contain_element(self, locator, limit=1):
        """Verifies that element 'locator' is found on the current page.
        The 'limit' argument can used to define how many elements the page should contain."""
        element = self.driver.find_elements(*locator)
        count = len(element)
        if not count == limit:
            raise AssertionError("Page should have contained {} element(s), but did contain {}.".format(limit, count))
        return element
    
    def input_text(self, locator, text):
        """Types the given 'text' into text field identified by 'locator'."""
        try:
            element = self.driver.find_element(*locator)
            element.clear()
            element.send_keys(text)
            element.send_keys(Keys.ENTER)
       
        except WebDriverException:
            print("Unable to locate {}".format(locator))

class Locators(object):
    """A class for main page locators. All locators should come here"""
    SEARCH_FIELD = (By.XPATH, "//form[@class='search']/input[@name='q']")

page = BrowserKeywords().open_browser("https://selenium-python.readthedocs.io")
assert "Selenium with Python" in page.title
element = ElementsKeywords(page).page_should_contain_element(Locators().SEARCH_FIELD)
ElementsKeywords(page).input_text(Locators().SEARCH_FIELD, "zabojnik")
assert "Your search did not match any documents." in page.page_source
page.close()