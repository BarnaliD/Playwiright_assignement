from behave import given, when, then

@given('User clicks on the reading list application')
def step_impl(context):
    context.page.goto('https://tap-vt25-testverktyg.github.io/exam--reading-list/')
    context.page.wait_for_selector('.catalog', timeout=10000)


@given('User has favorited a book')
def step_impl(context):
    # Favorite the first book
    first_book = context.page.locator('.book').first
    book_text = first_book.inner_text().replace('❤️', '').replace('💔', '').strip()
    
    if '"' in book_text:
        context.favorited_book_title = book_text.split('"')[1]
    else:
        context.favorited_book_title = book_text.split(',')[0]
    
    # Click to favorite
    first_book.locator('.star').click(force=True)
    context.page.wait_for_timeout(1000)
    
    # Verify it's favorited
    star = first_book.locator('.star')
    classes = star.get_attribute("class")
    assert "selected" in classes


@when('User clicks the favorite button again')
def step_impl(context):
    # Click the star button again to unfavorite
    first_book = context.page.locator('.book').first
    first_book.locator('.star').click(force=True)
    context.page.wait_for_timeout(1000)


@then('The book should be removed from favorites')
def step_impl(context):
    # Check the star is no longer selected
    first_book = context.page.locator('.book').first
    star = first_book.locator('.star')
    classes = star.get_attribute("class")
    assert "selected" not in classes
    
    # Go to favorites and verify the book is not there
    context.page.locator('[data-testid="favorites"]').click()
    context.page.wait_for_timeout(1000)
    
    favorite_books = context.page.locator('.book').all()
    
    # Extract titles from favorites
    titles = []
    for book in favorite_books:
        text = book.inner_text().replace('❤️', '').replace('💔', '').strip()
        if '"' in text:
            titles.append(text.split('"')[1])
        else:
            titles.append(text.split(',')[0])
    
    # The book should NOT be in favorites
    assert context.favorited_book_title not in titles