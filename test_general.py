import configparser
import pytest

from .pages.rest import verify_product_param_api
from .pages.cart import Cart
from .pages.home_page import Homepage
from .pages.signup import Signup
from .pages.login import Login
from .pages.logout import Logout



@pytest.mark.usefixtures('driver')
class TestSignInPage:
    # # Read configuration
    config = configparser.ConfigParser()
    config.read('config.ini')

    username = config['DEFAULT']['USERNAME']
    password = config['DEFAULT']['PASSWORD']

    # @pytest.mark.skip
    def test_ui_shopping(self, driver):


        # # Navigate to Homepage
        homepage_obj = Homepage()
        homepage_obj.navigate_to_homepage(driver)

        # Sign up task
        signup_obj = Signup()
        signup_obj.sign_up(driver, username=self.username, password=self.password)

        homepage_obj.navigate_to_homepage(driver)

        # Login task
        login_obj = Login()
        login_obj.login(driver, username=self.username, password=self.password)

        # Add two items in card
        homepage_obj.add_two_items_in_cart(driver, "Nexus 6")
        homepage_obj.navigate_to_laptoops_category(driver)
        homepage_obj.add_two_items_in_cart(driver, "MacBook Pro")

        # Navigate to cart
        cart_obj = Cart()
        cart_obj.navigate_to_cart(driver)

        # Verify two items
        cart_obj.verify_items(driver)
        cart_obj.verify_price(driver, 1750)

        # Navigate to Place order and enter information
        cart_obj.navigate_to_place_order(driver)

        # Create an order
        cart_obj.verify_order_price(driver, 1750)

        # # Logout
        logout_obj = Logout()
        logout_obj.logout(driver)


    # @pytest.mark.skip
    def test_clean_up(self, driver):
        config = configparser.ConfigParser()
        config.read('config.ini')
        ########################################
        # Login, observe cart and Logout
        ########################################
        # Navigate to home page
        homepage_obj = Homepage()
        homepage_obj.navigate_to_homepage(driver)

        # Login
        login_obj = Login()
        login_obj.login(driver, username=self.username, password=self.password)

        # Navigate to Cart
        cart_obj = Cart()
        cart_obj.navigate_to_cart(driver)

        # Delete all items / cleanup for correct price for future test
        cart_obj.delete_all_items(driver)

        # Logout
        logout_obj = Logout()
        logout_obj.logout(driver)


    # @pytest.mark.skip
    def test_another_shop_api(self, driver):
        ########################################
        # Pass 2
        ########################################

        # # Navigate to Homepage
        homepage_obj = Homepage()
        homepage_obj.navigate_to_homepage(driver)

        # Sign up task
        signup_obj = Signup()
        signup_obj.sign_up(driver, username=self.username, password=self.password)

        homepage_obj.navigate_to_homepage(driver)

        # Login task
        login_obj = Login()
        login_obj.login(driver, username=self.username, password=self.password)

        # Add two items in card
        homepage_obj.add_two_items_in_cart(driver, "Nexus 6")

        # Navigate to cart
        cart_obj = Cart()
        cart_obj.navigate_to_cart(driver)




        # Verify item patameters
    def test_validate_api_product(self):
        verify_product_param_api()












