"""[summary]
    """
from behave import given, step, then, when
from behave.runner import Context
from src.features.helpers import configuration


@given("I am not logged in")
def step_not_logged_in(context: Context):
    """[summary]

    Args:
        context (Context): [description]
    """
    pass


@then('I should see the English option')
def step_should_see_option(context: Context):
    """[summary]

    Args:
        context (Context): [description]
    """
    link = context.browser.find_element_by_link_text("English")
    assert True is True


@when("I search cats")
def step_search_cats(context: Context):
    """[summary]

    Args:
        context (Context): [description]
    """
    search = context.browser.find_element_by_id("searchInput")
    search.send_keys("cats")
    search.submit()


@then("I should go to the cats page")
def step_impl(context: Context):
    """[summary]

    Args:
        context (Context): [description]
    """
    title = context.browser.find_element_by_tag_name("h1")
    assert "Cat" in title.text
