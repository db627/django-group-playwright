import re
from playwright.sync_api import Page, expect
from playwright.sync_api import Playwright, sync_playwright, expect



def test_view_all_todos():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8000/todo")
        # Verify if all items are displayed
        assert page.text_content("a")  # Modify as needed to verify list content
        browser.close()
