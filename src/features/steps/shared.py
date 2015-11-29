import behave
from selenium import webdriver
from helpers import configuration

@given("I am on the homepage")
@when("I am on the homepage")
def step_impl(context):
    context.browser.get(configuration.get_setting("tests", "url"))