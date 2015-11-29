import behave
from selenium import webdriver
from helpers import configuration
from selenium.webdriver.common.keys import Keys

@given("I am not logged in")
def step_impl(context):
    pass

@when("I am on the homepage")
def step_impl(context):
    context.browser.get(configuration.get_setting("tests", "url"))

@then('I should see the English option')
def step_impl(context):
    link = context.browser.find_element_by_link_text("English")
    assert True is True