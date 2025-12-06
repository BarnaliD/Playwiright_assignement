from playwright.sync_api import sync_playwright

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=True) 

def before_scenario(context, scenario):
    context.page = context.browser.new_page()

def after_scenario(context, scenario):
    if hasattr(context, 'page'):
        context.page.close()

def after_all(context):
    if hasattr(context, 'browser'):
        context.browser.close()
    if hasattr(context, 'playwright'):
        context.playwright.stop()