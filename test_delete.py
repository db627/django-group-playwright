import re
from playwright.sync_api import Page, expect
from playwright.sync_api import Playwright, sync_playwright, expect


def test_delete(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:8000/todo/")
    page.get_by_role("link", name="Delete").nth(4).click()

    context.close()
    browser.close()





with sync_playwright() as playwright:
    test_delete(playwright)