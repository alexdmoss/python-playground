# `brew install chromedriver` (or equivalent) and allow it in security settings
import pytest

from selenium import webdriver

url = 'https://alexos.dev/contact/'

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_homepage(browser):
    browser.get(url)
    src = browser.page_source
    assert 'Cloud Platforms' in src
