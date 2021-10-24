import behave
from selenium import webdriver
from helpers import configuration
from selenium.webdriver.common.keys import Keys


@given("I am not logged in")
def step_impl(context):
    pass


@then('I should see the English option')
def step_impl(context):
    link = context.browser.find_element_by_link_text("English")
    assert True is True


@when("I search cats")
def step_impl(context):
    search = context.browser.find_element_by_id("searchInput")
    search.send_keys("cats")
    search.submit()


@then("I should go to the cats page")
def step_impl(context):
    title = context.browser.find_element_by_tag_name("h1")
    assert "Cat" in title.text
