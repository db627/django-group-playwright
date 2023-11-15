import re
from playwright.sync_api import Page, expect
from playwright.sync_api import Playwright, sync_playwright, expect

def test_update_todo():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto("http://localhost:8000/todo/")
        page.get_by_role("link", name="Update").first.click()
        page.get_by_label("Todo item:").fill("Item3")
        page.get_by_role("button", name="Update Todo Item").click()

        assert "Item3" in page.text_content("body"), "Update operation failed"

        browser.close()
