from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def set_up():
    selenium = webdriver.Chrome(executable_path=r'C:\Users\petra.zabojnikova\Documents\myProjects\study\TestLadies\chromedriver_win32\chromedriver.exe')
    return selenium

def tear_down(selenium):
    selenium.quit()  

def main():
    browser = set_up()    
    browser.get("https://selenium-python.readthedocs.io")
    assert "Selenium with Python" in browser.title
    el = browser.find_element_by_name('q')
    el.clear()
    el.send_keys("zabojnik")
    el.send_keys(Keys.ENTER)
    assert "Your search did not match any documents." in browser.page_source
    tear_down(browser)

main()