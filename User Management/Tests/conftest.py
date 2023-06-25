import pytest
from playwright.sync_api import Page

@pytest.fixture
def navigation(page:Page):
        page.goto("http://192.168.1.53:3000/users")
        