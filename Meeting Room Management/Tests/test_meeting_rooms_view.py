import pytest
from playwright.sync_api import Page

def test_meeting_rooms_view(navigation, page:Page, headless=False):
    meeting_rooms_btn = page.locator("xpath = //*[@id='root']/div/div/div/ul/a[2]/li/div")
    assert(meeting_rooms_btn.is_enabled())
    meeting_rooms_btn.click()
    assert(page.url.__eq__("http://3.19.1.104/meetingrooms"))
    assert(page.locator("#title").inner_text() == "Meeting Rooms")
