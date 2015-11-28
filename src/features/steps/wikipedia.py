import behave
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@given("I am not logged in")
def step_impl(context):
    pass

@when("I am on the homepage")
def step_impl(context):
    context.browser.get("http://wikipedia.org")

@then('I should see the English option')
def step_impl(context):
    link = context.browser.find_element_by_link_text("English")
    assert True is True