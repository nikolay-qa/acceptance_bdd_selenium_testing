import behave


behave.use_step_matcher('re')


@behave.when('I click on the link with id "(.+)"')
def step_impl(context, link_id):
    button = context.driver.find_element_by_id(link_id)
    button.click()
