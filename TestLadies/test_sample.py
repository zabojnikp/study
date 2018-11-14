from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
#set up a browser
@pytest.fixture
def selenium(base_url):
    selenium = webdriver.Chrome('chromedriver')
    selenium.get(base_url)
    selenium.maximize_window()
    selenium.set_page_load_timeout('10')
    return selenium   

def test_search(selenium, variables):  
    step_1(selenium, variables['input_text'])
    step_2(selenium, variables['input_text'])
    step_3(selenium)

#input term in search field and submit
def step_1(selenium, input_text):
    search_bar = selenium.find_element_by_id('q')
    search_bar.send_keys(input_text)
    search_bar.send_keys(Keys.ENTER)

#verify text is found
def step_2(selenium, input_text):
    element = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.ID, "col-annot"))
    )
    assert 'Výsledek vyhledávání výrazu ' + input_text in element.text
    assert element.is_displayed() is True


#teardown
def step_3(selenium):
    selenium.quit()
