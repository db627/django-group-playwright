import re
from playwright.sync_api import Page, expect
from playwright.sync_api import Playwright, sync_playwright, expect

def test_add_todo():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto("http://localhost:8000/todo/")
        page.get_by_role("link", name="Add New Todo").click()
        page.get_by_label("Todo item:").fill("NewItem")
        page.get_by_role("button", name="Add Todo Item").click()

        assert "NewItem" in page.text_content("body"), "Add operation failed"

        browser.close()
