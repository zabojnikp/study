from selenium import webdriver
from selenium.webdriver.support.ui import Select

def set_up():
    selenium = webdriver.Chrome(executable_path=r'C:\Users\petra.zabojnikova\Documents\myProjects\study\TestLadies\chromedriver_win32\chromedriver.exe')
    return selenium

def tear_down(selenium):
    selenium.quit()

def test_main():
    options = []
    cookies = dict()
    browser = set_up()
    browser.get("https://premium.formfactory.cz/rozvrh/")
    # checking cookies
    cookie = {'name' : 'foo', 'value' : 'bar'}
    browser.add_cookie(cookie)
    cookies = browser.get_cookies()
    assert "Rozvrh" in browser.title
    browser.maximize_window()
    #checking options
    element = browser.find_element_by_id("programy")
    all_options = element.find_elements_by_tag_name("option")
    for option in all_options:
        options.append(option)
        option.click()
    return cookies, options

print(test_main())
tear_down(set_up())
