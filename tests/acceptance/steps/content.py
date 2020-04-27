import behave

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.blog_page import BlogPage

behave.use_step_matcher('re')


@behave.then('Title is shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed()


@behave.step('The title tag has content "(.+)"')
def step_impl(context, tag_content):
    page = BasePage(context.driver)
    assert page.title.text == tag_content


@behave.then('I can see there is a posts section on the page')
def step_impl(context):
    page = BlogPage(context.driver)
    assert page.posts_section.is_displayed()


@behave.then('I can see there is a post with title "(.+)" in the posts section')
def step_impl(context, post_title):
    page = BlogPage(context.driver)
    post_with_title = [post for post in page.posts if post.text == post_title]
    assert len(post_with_title) > 0
    assert all([post.is_displayed() for post in post_with_title])
