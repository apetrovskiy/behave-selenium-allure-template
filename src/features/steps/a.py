from behave import given, step
from behave.runner import Context


@step('step 0001')
@given(u'ccc')
def step_impl(context: Context):
    # raise NotImplementedError(u'STEP: Given ccc')
    pass
