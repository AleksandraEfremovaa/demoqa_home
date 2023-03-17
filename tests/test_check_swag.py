from pages.swag_labs import Swag
def test_exist_icon(browser):
    swag_page = Swag(browser)
    swag_page.visit()
    swag_page.exist_icon()
    swag_page.exist_username()
    swag_page.exist_password_field()
