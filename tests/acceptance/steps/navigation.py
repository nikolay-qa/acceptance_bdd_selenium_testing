import behave
from selenium import webdriver

behave.use_step_matcher('re')


@behave.given('I am on the homepage')
def step_impl(context):
    browser = webdriver.Chrome()
    browser.get('http://127.0.0.1:5000')