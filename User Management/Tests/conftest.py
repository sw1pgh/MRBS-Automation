import pytest
from playwright.sync_api import Page

@pytest.fixture
def navigation(page:Page):
        page.goto("http://3.19.1.104/users")
        