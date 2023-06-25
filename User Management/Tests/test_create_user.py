import pytest
from playwright.sync_api import Page

def test_right_create_user(navigation, page:Page, headless=False):

    users_btn = page.locator("xpath = //*[@id='root']/div/div/div/ul/a[3]/li/div")
    create_btn=page.locator("#create-btn")
    name_field=page.locator("#\:r1\:")
    email_field=page.locator("#\:r3\:")
    emp_Id=page.locator("#\:r5\:")
    role=page.locator("#mui-component-select-role")
    admin=page.locator("xpath = //*[@id='menu-role']/div[3]/ul/li[1]")
    user=page.locator("xpath = //*[@id='menu-role']/div[3]/ul/li[2]")
    save_btn=page.locator("#save-btn")
    close_btn=page.locator("#close-btn")
    noti=page.locator("#notification-msg")
    
    assert(users_btn.is_enabled())
    users_btn.click()

    assert(create_btn.is_enabled())
    create_btn.click()

    assert(name_field.is_editable())
    name_field.click()
    name_field.fill("Swapnaneel Ghosh")

    assert(email_field.is_editable())
    email_field.click()
    email_field.fill("swjdjiel.ghosh@geotechinfo.net")

    assert(emp_Id.is_enabled())
    emp_Id.click()
    emp_Id.fill("GIPL/186")

    assert(role.is_enabled())
    role.click()
    user.click()

    assert(save_btn.is_enabled())
    save_btn.click()

    assert(noti.inner_text()=="User has been created successfully")

def test_wrong_create_user(navigation, page:Page, headless=False):

    users_btn = page.locator("xpath = //*[@id='root']/div/div/div/ul/a[3]/li/div")
    create_btn=page.locator("#create-btn")
    name_field=page.locator("#\:r1\:")
    email_field=page.locator("#\:r3\:")
    emp_Id=page.locator("#\:r5\:")
    role=page.locator("#mui-component-select-role")
    admin=page.locator("xpath = //*[@id='menu-role']/div[3]/ul/li[1]")
    user=page.locator("xpath = //*[@id='menu-role']/div[3]/ul/li[2]")
    save_btn=page.locator("#save-btn")
    close_btn=page.locator("#close-btn")
    
    assert(users_btn.is_enabled())
    users_btn.click()

    assert(create_btn.is_enabled())
    create_btn.click()

    assert(name_field.is_editable())
    name_field.click()
    name_field.fill("Swapnaneel Ghosh")

    assert(email_field.is_editable())
    email_field.click()
    email_field.fill("swapnaneel.ghosh")

    assert(emp_Id.is_enabled())
    emp_Id.click()
    emp_Id.fill("GIPL/239")

    assert(role.is_enabled())
    role.click()
    user.click()

    assert(save_btn.is_enabled())
    save_btn.click()
    
    page.on("dialog", lambda dialog: dialog.accept())