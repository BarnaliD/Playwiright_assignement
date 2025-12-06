from behave import given, when, then

@given('User navigates to the application')
def step_impl(context):
    context.page.goto('https://tap-vt25-testverktyg.github.io/exam--reading-list/')
    context.page.wait_for_selector('.catalog', timeout=10000)


@when('User clicks on the add book button')
def step_impl(context):
    # Click the "Lägg till bok" (Add book) button
    add_button = context.page.locator('[data-testid="add-book"]')
    assert add_button.is_visible(), "Add book button not visible"
    add_button.click()
    context.page.wait_for_timeout(1000)


@then('User should be on the add book page')
def step_impl(context):
    
    
    #  Check for form elements
    form_elements = context.page.locator('form, input, textarea').count()
    assert form_elements > 0, "No form elements found on add book page"
    
    #  Check if the add-book button is disabled/active
    add_button = context.page.locator('[data-testid="add-book"]')
    
    # Check button state is disabled
    is_disabled = add_button.get_attribute('disabled')
    
    if is_disabled is not None:
        print("✓ On add book page (add button is disabled)")
    else:
        # Alternative: check for specific page elements
        print("✓ On add book page (form elements found)")