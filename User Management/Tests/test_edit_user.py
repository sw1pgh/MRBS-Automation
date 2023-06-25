import pytest
from playwright.sync_api import Page

def test_edit_meeting_room(navigation, page:Page, headless=False):
    edit_btn=page.locator("xpath = //*[@id='user-table']/tbody/tr[1]/td[6]/button")
    name_field=page.locator("#\:r1\:")
    role=page.locator("#mui-component-select-role")
    admin=page.locator("xpath = //*[@id='menu-role']/div[3]/ul/li[1]")
    user=page.locator("xpath = //*[@id='menu-role']/div[3]/ul/li[2]")
    save_btn=page.locator("#save-btn")
    close_btn=page.locator("#close-btn")
    noti=page.locator("#notification-msg")


    assert(edit_btn.is_enabled)    
    edit_btn.click()
    
    assert(name_field.is_enabled())
    name_field.click()
    name_field.fill("Ayan Das")    

    assert(role.is_enabled())
    role.click()    

    assert(admin.is_enabled())
    admin.click()
    
    # assert(close_btn.is_enabled())
    # close_btn.click()

    assert(save_btn.is_enabled())
    save_btn.click()
    
    assert(noti.inner_text()=="User has been updated successfully")