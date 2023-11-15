import re
from playwright.sync_api import Page, expect
from playwright.sync_api import Playwright, sync_playwright, expect

def test_delete_todo():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto("http://localhost:8000/todo/")
        page.get_by_role("link", name="Delete").first.click()

        assert "Item3" not in page.text_content("body"), "Deletion operation failed"

        browser.close()
