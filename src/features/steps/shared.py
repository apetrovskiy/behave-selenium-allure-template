from behave import given, when
from behave.runner import Context
from src.features.helpers import configuration


@given("I am on the homepage")
@when("I am on the homepage")
def step_impl(context: Context):
    context.browser.get(configuration.get_setting("tests", "url"))
