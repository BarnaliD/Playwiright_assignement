from behave import given, when, then

@given('User is on the application page')
def step_impl(context):
    context.page.goto('https://tap-vt25-testverktyg.github.io/exam--reading-list/')
    context.page.wait_for_selector('[data-testid="add-book"]', timeout=10000)


@when('User clicks on the button for adding the book')
def step_impl(context):
    context.page.locator('[data-testid="add-book"]').click()
    context.page.wait_for_timeout(500)


@when('User fills in the book details')
def step_impl(context):
    context.new_book_title = "Behave Test Book"
    context.new_book_author = "QA Automation"

    context.page.locator('[data-testid="add-input-title"]').fill(context.new_book_title)
    context.page.locator('[data-testid="add-input-author"]').fill(context.new_book_author)


@when('User submits the book form')
def step_impl(context):
    context.page.locator('[data-testid="add-submit"]').click()
    context.page.wait_for_timeout(1000)


@then('The new book should appear in the catalog')
def step_impl(context):
    # Navigate back to catalog
    catalog_button = context.page.locator('[data-testid="catalog"]')
    if not catalog_button.get_attribute('disabled'):
        catalog_button.click()
        context.page.wait_for_timeout(1000)
    
    # Check for the book
    books = context.page.locator('.book').all()
    
    book_found = False
    for book in books:
        book_text = book.inner_text()
        if context.new_book_title in book_text and context.new_book_author in book_text:
            book_found = True
            break

    assert book_found, f"Book '{context.new_book_title}' not found in catalog"