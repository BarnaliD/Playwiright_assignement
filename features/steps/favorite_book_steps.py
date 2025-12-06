from behave import given, when, then

@given('User goes to the reading list application')
def step_impl(context):
    context.page.goto('https://tap-vt25-testverktyg.github.io/exam--reading-list/')
    context.page.wait_for_selector('.catalog', timeout=10000)


@when('User clicks the favorite button on a book')
def step_impl(context):
    # Get first book and its title
    first_book = context.page.locator('.book').first
    book_text = first_book.inner_text().replace('❤️', '').replace('💔', '').strip()
    
    # Extract title between quotes
    if '"' in book_text:
        context.favorited_book_title = book_text.split('"')[1]
    else:
        context.favorited_book_title = book_text.split(',')[0]
    
    # Click favorite button
    first_book.locator('.star').click(force=True)
    context.page.wait_for_timeout(1000)


@then('The book should be marked as favorite')
def step_impl(context):
    star = context.page.locator('.book').first.locator('.star')
    classes = star.get_attribute("class")
    assert "selected" in classes


@then('The book should appear in the favorites list')
def step_impl(context):
    # Go to favorites
    context.page.locator('[data-testid="favorites"]').click()
    context.page.wait_for_timeout(1000)
    
    # Check if our book is there
    favorite_books = context.page.locator('.book').all()
    assert len(favorite_books) > 0
    
    # Extract titles safely
    titles = []
    for book in favorite_books:
        text = book.inner_text().replace('❤️', '').replace('💔', '').strip()
        if '"' in text:
            titles.append(text.split('"')[1])
        else:
            titles.append(text.split(',')[0])
    
    assert context.favorited_book_title in titles