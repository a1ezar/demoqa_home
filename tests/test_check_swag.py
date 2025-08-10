from pages.swag_labs import SwagLabs


def test_check_icon(browser):
    swag_lab_page = SwagLabs(browser)
    swag_lab_page.visit()
    assert swag_lab_page.exist_icon()


def test_check_username(browser):
    swag_lab_page = SwagLabs(browser)
    swag_lab_page.visit()
    assert swag_lab_page.exist_username_field()
    
    
def test_check_password(browser):
    swag_lab_page = SwagLabs(browser)
    swag_lab_page.visit()
    assert swag_lab_page.exist_password_field()

