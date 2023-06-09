from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchFrameException

class Swag(BasePage):

    def exist_icon(self):

        try:
            self.find_element(locator='div.login_logo')
        except NoSuchFrameException:
            return False
        return True

    def exist_username(self):
        try:
            self.find_element(locator='#user-name')
        except NoSuchFrameException:
            return False
        return True

    def exist_password_field(self):
        try:
            self.find_element(locator='#password')
        except NoSuchFrameException:
            return False
        return True



