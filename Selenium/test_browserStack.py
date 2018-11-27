from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_cap = {
    'browser': 'Chrome',
    'browser_version': '62.0',
    'os': 'Windows',
    'os_version': '10',
    'resolution': '1024x768'
}

selenium = webdriver.Remote(
command_executor='http://petrazabojnikova1:38jSqGm9zk6cqFUH9Xzf@hub.browserstack.com:80/wd/hub',
desired_capabilities=desired_cap)
selenium.get("https://selenium-python.readthedocs.io")
assert "Selenium with Python" in selenium.title
el = selenium.find_element_by_name('q')
el.clear()
el.send_keys("zabojnik")
el.send_keys(Keys.ENTER)
assert "Your search did not match any documents." in selenium.page_source
selenium.quit()
