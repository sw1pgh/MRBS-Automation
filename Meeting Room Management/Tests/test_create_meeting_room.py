import pytest
from playwright.sync_api import Page

def test_right_create_meeting_room(navigation, page:Page, headless=False):

    meeting_rooms_btn = page.locator("xpath = //*[@id='root']/div/div/div/ul/a[2]/li/div")
    capacity_field=page.locator("xpath = /html/body/div[3]/div[3]/form/div/div[2]/div/div/input")
    name_field=page.locator("xpath = /html/body/div[3]/div[3]/form/div/div[1]/div/div/input")
    create_btn=page.locator("#create-btn")
    status=page.locator("#mui-component-select-status")
    active = page.locator("xpath = //*[@id='menu-status']/div[3]/ul/li[1]")
    inactive=page.locator("xpath = //*[@id='menu-status']/div[3]/ul/li[2]")
    save_btn=page.locator("#save-btn")
    close_btn=page.locator("#close-btn")
    noti=page.locator("#notification-msg")

    assert(meeting_rooms_btn.is_enabled())    
    meeting_rooms_btn.click()    

    assert(create_btn.is_enabled())
    create_btn.click()    

    assert(name_field.is_enabled())
    name_field.click()
    name_field.fill("Souvik's Eternal Space")    

    assert(capacity_field.is_editable())
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
    
    assert(noti.inner_text()=="Meeting Room has been created successfully")
    

def test_wrong_create_meeting_room(navigation, page:Page, headless=False):

    capacity_field=page.locator("xpath = /html/body/div[3]/div[3]/form/div/div[2]/div/div/input")
    name_field=page.locator("xpath = /html/body/div[3]/div[3]/form/div/div[1]/div/div/input")
    create_btn=page.locator("#create-btn")
    status=page.locator("#mui-component-select-status")
    active = page.locator("xpath = //*[@id='menu-status']/div[3]/ul/li[1]")
    inactive=page.locator("xpath = //*[@id='menu-status']/div[3]/ul/li[2]")
    save_btn=page.locator("#save-btn")
    close_btn=page.locator("#close-btn")

    assert(create_btn.is_enabled())
    create_btn.click()   

    assert(name_field.is_editable())
    name_field.click()
    name_field.fill("Eden Gardens") 

    assert(capacity_field.is_editable())
    capacity_field.click()
    capacity_field.fill("22")    

    assert(status.is_enabled())
    status.click()    

    assert(inactive.is_enabled())
    inactive.click()
    
    assert(save_btn.is_enabled())
    save_btn.click()

    page.on("dialog", lambda dialog: dialog.accept())
        