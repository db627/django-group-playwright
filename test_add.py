import re
from playwright.sync_api import Page, expect
from playwright.sync_api import Playwright, sync_playwright, expect

def test_add(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:8000/todo/")
    page.get_by_role("link", name="Add New Todo").click()
    page.get_by_label("Todo item:").click()
    page.get_by_label("Todo item:").fill("item")

with sync_playwright() as playwright:
    test_add(playwright)