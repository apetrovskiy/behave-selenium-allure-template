from behave import given, step, then, when
from behave.runner import Context
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from src.features.helpers import configuration


@given("I am not logged in")
def step_impl(context: Context):
    pass


@then('I should see the English option')
def step_impl(context: Context):
    link = context.browser.find_element_by_link_text("English")
    assert True is True


@when("I search cats")
def step_impl(context: Context):
    search = context.browser.find_element_by_id("searchInput")
    search.send_keys("cats")
    search.submit()


@then("I should go to the cats page")
def step_impl(context: Context):
    title = context.browser.find_element_by_tag_name("h1")
    assert "Cat" in title.text
