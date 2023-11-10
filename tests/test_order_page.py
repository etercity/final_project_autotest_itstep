import pytest
from ..pages.base_page import BasePage
from ..pages.order_page import OrderPage
from ..pages.signup_login_page import SignupLoginPage
from ..settings import sets
import random


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.order_page
class TestMainPage:

    def setup_method(self):
        hash_name = "%032x" % random.getrandbits(128)
        self.email_for_subscribe = f"{hash_name}@mail.com"

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def test_login_to_cabinet(self, browser):
        self.link_to_cabinet = browser.current_url
        page = SignupLoginPage(browser, self.link_to_cabinet)
        page.click_button_signup_login()
        page.explicit_wait(2)
        page.input_email_password(sets.TEST_EMAIL, sets.PASSWORD)
        page.press_button_login()
        page.is_alert_success_after_subscribe()
        page.is_button_logout_in_header()
        page = OrderPage(browser, self.link_to_cabinet)
        page.click_on_logo()

    def test_add_products_to_cart(self, browser):
        self.link_to_cabinet = browser.current_url
        page = OrderPage(browser, self.link_to_cabinet)
        page.add_to_cart_first_product()
        page.explicit_wait(2)
        page.press_btn_continue_shop_popup()
        page.explicit_wait(1)
        page.add_to_cart_second_product()

    def test_checkout(self, browser):
        self.link_to_cabinet = browser.current_url
        page = OrderPage(browser, self.link_to_cabinet)
        page.press_btn_checkout_popup()
        page.add_notice()
        page.press_green_btn_checkout()
        page.is_alert_success()
        page.explicit_wait(5)

















