from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Homepage:
    def __new__(cls, *args, **kwargs):
        return super(Homepage, cls).__new__(cls, *args, **kwargs)

    def navigate_to_homepage(self, driver):
        driver.get("https://www.demoblaze.com/")
        driver.implicitly_wait(10)
        driver.get_screenshot_as_file(f'./images/{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.png')

    def navigate_to_laptoops_category(self, driver):
        laptoop = driver.find_element(By.XPATH, "//a[text()='Laptops']")
        laptoop.click()

    def add_two_items_in_cart(self, driver, item_1):
        self.add_one_item_in_cart(driver, item_1)
        self.click_on_home_toolbar(driver)

    def add_one_item_in_cart(self, driver, param):
        # pause before moving on
        item_one = WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.XPATH, f"//a[text()='{param}']"))
        item_one.click()

        addtocart = driver.find_element(By.XPATH, '//a[@class="btn btn-success btn-lg"]')
        addtocart.click()

        wait = WebDriverWait(driver, 10)
        wait.until(EC.alert_is_present())

        alert = Alert(driver)
        alert.accept()

    def click_on_home_toolbar(self, driver):
        home = driver.find_element(By.XPATH, '//a[@class="nav-link"]')
        home.click()
