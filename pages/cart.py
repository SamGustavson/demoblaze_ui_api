import time
from time import sleep


from selenium.webdriver.common.by import By

from pages.rest import verify_product, verify_items_count_and_get_product_id, get_user_cookie_via_login


class Cart:
    def __new__(cls, *args, **kwargs):
        return super(Cart, cls).__new__(cls, *args, **kwargs)

    def navigate_to_cart(self, driver):
        cart = driver.find_element(By.ID, "cartur")
        cart.click()

    def navigate_to_place_order(self, driver):
        # verify that page is looking at cart
        placeorder = driver.find_element(By.XPATH, '//button[text()="Place Order"]')
        placeorder.click()

        name = driver.find_element(By.ID, 'name')
        name.send_keys("Alex Fox")

        country = driver.find_element(By.ID, 'country')
        country.send_keys("Ukraine")

        city = driver.find_element(By.ID, 'city')
        city.send_keys("Vinnytsia")

        card = driver.find_element(By.ID, 'card')
        card.send_keys("0123456789")

        month = driver.find_element(By.ID, 'month')
        month.send_keys("September")

        year = driver.find_element(By.ID, 'year')
        year.send_keys("2022")

        purchase_btn = driver.find_element(By.XPATH, '//button[contains(text(),"Purchase")]')
        purchase_btn.click()



    def verify_order_price(self, driver,order_total:int ):

        order_confirmation = driver.find_element(By.XPATH, '//p[contains(text(),"Id:")]').text
        print(f' Order Confirmation:\n{order_confirmation}')
        assert str(order_total) in order_confirmation
        print(f'Order Total: {order_total} is confirmed')
        sleep(0.25)
        driver.find_element(By.XPATH, '//button[contains(text(),"OK")]').click()

        ok_button = driver.find_element(By.XPATH, '//div[button[text()="Purchase"]]/button[text()="Close"]')
        ok_button.click()

    def verify_items(self, driver):
        product_list = []
        for p in product_list:
            item_in_cart = driver.find_element(By.XPATH, f'//td[contains(.,"{p}")]').is_displayed()
            assert item_in_cart
            print(f'Success! {p} is in Shopping Cart: {item_in_cart}')
            sleep(0.25)

    def verify_price(self, driver, price:int):
        driver.implicitly_wait(5)
        time.sleep(3)
        total_price = driver.find_element(By.ID, 'totalp').text
        print(f'Validate Cart Total:\nExpected cart total: {price}, Actual cart total: {total_price} ')
        assert str(price) == total_price


    def delete_one_item(self, driver):
        deleteitem = driver.find_element(By.XPATH, '(//a[text()="Delete"])[1]')
        deleteitem.click()


    def delete_x_items(self, driver, number_of_items):
        for _ in range(number_of_items):
            self.delete_one_item(driver)
            time.sleep(driver)


    def delete_all_items(self, driver):
        list_items = []
        items = driver.find_elements(By.XPATH, '(//a[text()="Delete"])')
        for item in items:
            text = item.text
            list_items.append(text)
        print("List items deleted:", list_items)
        for i in list_items :
            self.delete_one_item(driver)
            time.sleep(2)

def verify_product_param_api():
    verify_product(verify_items_count_and_get_product_id(get_user_cookie_via_login()))