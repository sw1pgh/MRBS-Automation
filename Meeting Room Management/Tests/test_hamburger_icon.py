import pytest
from playwright.sync_api import Page

def test_hamburger_icon(navigation, page:Page, headless=False):
    ham_btn = page.locator("xpath = //*[@id='root']/div/header/div/button")
    my_calendar_btn = page.locator("xpath = //*[@id='root']/div/div/div/ul/a[1]/li/div")
    meeting_rooms_btn = page.locator("xpath=//*[@id='root']/div/div/div/ul/a[2]/li/div")
    manage_users_btn = page.locator("xpath = //*[@id='root']/div/div/div/ul/a[3]/li/div")
    assert(ham_btn.is_visible())
    ham_btn.click()
    assert(my_calendar_btn.is_enabled())
    assert(meeting_rooms_btn.is_enabled())
    assert(manage_users_btn.is_enabled())


