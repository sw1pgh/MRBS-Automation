import pytest
from playwright.sync_api import Page

def test_users_view_page(navigation, page:Page, headless=False):
    users_btn = page.locator("xpath = //*[@id='root']/div/div/div/ul/a[3]/li/div")
    assert(users_btn.is_enabled())
    users_btn.click()
    assert(page.url.__eq__("http://192.168.1.53:3000/users"))
    assert(page.locator("xpath = //*[@id='root']/div/main/div[2]/div/div/h2").inner_text() == "Users")
