import pytest
from playwright.sync_api import Page

def test_right_edit_meeting_room(navigation, page:Page, headless=False):
    edit_btn=page.locator("xpath = //*[@id='meeting-room-table']/tbody/tr[1]/td[4]/button")
    name_field=page.locator("#\:r0\:")
    capacity_field=page.locator("#\:r1\:")    
    status=page.locator("#mui-component-select-status")
    active = page.locator("xpath = //*[@id='menu-status']/div[3]/ul/li[1]")
    inactive=page.locator("xpath = //*[@id='menu-status']/div[3]/ul/li[2]")
    save_btn=page.locator("#save-btn")
    close_btn=page.locator("#close-btn")
    noti=page.locator("#notification-msg")


    assert(edit_btn.is_enabled)    
    edit_btn.click()
    
    assert(name_field.is_enabled())
    name_field.click()
    name_field.fill("SSG")    

    assert(capacity_field.is_enabled())
    capacity_field.click()
    capacity_field.fill("10")    

    assert(status.is_enabled())
    status.click()    

    assert(active.is_enabled())
    active.click()
    
    # assert(close_btn.is_enabled())
    # close_btn.click()

    assert(save_btn.is_enabled())
    save_btn.click()
    
    assert(noti.inner_text()=="Meeting Room has been Updated successfully")


def test_wrong_meeting_room(navigation, page:Page, headless=False):
    edit_btn=page.locator("xpath = //*[@id='meeting-room-table']/tbody/tr[1]/td[4]/button")
    name_field=page.locator("#\:r0\:")
    capacity_field=page.locator("#\:r1\:")    
    status=page.locator("#mui-component-select-status")
    active = page.locator("xpath = //*[@id='menu-status']/div[3]/ul/li[1]")
    inactive=page.locator("xpath = //*[@id='menu-status']/div[3]/ul/li[2]")
    save_btn=page.locator("#save-btn")
    close_btn=page.locator("#close-btn")


    assert(edit_btn.is_enabled)    
    edit_btn.click()
    
    assert(name_field.is_enabled())
    name_field.click()
    name_field.fill("Melbourne")    

    assert(capacity_field.is_enabled())
    capacity_field.click()
    capacity_field.fill("23")    

    assert(status.is_enabled())
    status.click()    

    assert(active.is_enabled())
    active.click()
    
    # assert(close_btn.is_enabled())
    # close_btn.click()

    assert(save_btn.is_enabled())
    save_btn.click()
    
    page.on("dialog", lambda dialog: dialog.accept())