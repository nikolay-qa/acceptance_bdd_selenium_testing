import behave
from tests.acceptance.page_model.base_page import BasePage

behave.use_step_matcher('re')


@behave.then('Title is shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed()


@behave.step('The title tag has content "(.+)"')
def step_impl(context, tag_content):
    page = BasePage(context.driver)
    assert page.title.text == tag_content

