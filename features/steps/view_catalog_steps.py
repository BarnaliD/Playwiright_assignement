from behave import given, then

@given('User open the reading list application')
def step_impl(context):
    context.page.goto('https://tap-vt25-testverktyg.github.io/exam--reading-list/')
    context.page.wait_for_load_state('networkidle')
    context.page.wait_for_selector('.catalog', timeout=10000)


@then('User should see a list of books')
def step_impl(context):
    books = context.page.locator('.book').all()
    assert len(books) > 0, 'No books found on the page'


@then('at least one book should be visible')
def step_impl(context):
    books = context.page.locator('.book').all()
    visible_books = [b for b in books if b.is_visible()]
    assert len(visible_books) > 0, 'No visible books found'