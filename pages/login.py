import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Login:
    def __new__(cls, *args, **kwargs):
        return super(Login, cls).__new__(cls, *args, **kwargs)

    def login(self, driver, username, password):
        logbutton = driver.find_element(By.ID, "login2")
        logbutton.click()

        loginun = WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.ID, "loginusername"))
        loginun.send_keys(username)

        loginpw = driver.find_element(By.ID, "loginpassword")
        loginpw.send_keys(password)

        loginbutton = driver.find_element(By.XPATH, "//button[text() = 'Log in']")
        loginbutton.click()

        # pause before moving on
        time.sleep(2)
