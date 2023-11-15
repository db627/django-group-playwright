import re
from playwright.sync_api import Page, expect
from playwright.sync_api import Playwright, sync_playwright, expect


def test_todo_crud_operations():
    with sync_playwright() as playwright:
        # Launch the browser
        browser = playwright.chromium.launch(headless=True)  # Set headless to False if you want to see the browser actions
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the ToDo list page
        page.goto("http://localhost:8000/todo/")
        assert page.url == "http://localhost:8000/todo/", "Did not navigate to the ToDo list page"

        # Update an existing ToDo item
        page.get_by_role("link", name="Update").first.click()
        page.get_by_label("Todo item:").fill("Item3")
        page.get_by_role("button", name="Update Todo Item").click()
        # Add an assertion to verify the update
        assert "Item3" in page.text_content("body"), "Update operation failed"

        # Delete a ToDo item
        page.get_by_role("link", name="Delete").first.click()
        # Add an assertion to verify deletion
        assert "Item3" not in page.text_content("body"), "Deletion operation failed"

        # Add a new ToDo item
        page.get_by_role("link", name="Add New Todo").click()
        page.get_by_label("Todo item:").fill("NewItem")
        page.get_by_role("button", name="Add Todo Item").click()
        # Add an assertion to verify the new item was added
        assert "NewItem" in page.text_content("body"), "Add operation failed"

        # Clean up
        browser.close()
