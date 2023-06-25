import pytest
from playwright.sync_api import Page

def test_title(navigation,page:Page, headless=False):
        assert page.title() == "MRBS"

        