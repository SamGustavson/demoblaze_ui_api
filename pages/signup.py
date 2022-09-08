from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Signup:
    def __new__(cls, *args, **kwargs):
        return super(Signup, cls).__new__(cls, *args, **kwargs)

    def sign_up(self, driver, username, password):
        element = driver.find_element(By.ID, "signin2")
        element.click()

        driver.find_element(By.ID, "sign-username").send_keys(username)

        driver.find_element(By.ID, "sign-password").send_keys(password)


        signup = driver.find_element(By.XPATH, "//button[text() = 'Sign up']")
        signup.click()

        wait = WebDriverWait(driver, 10)
        wait.until(EC.alert_is_present())

        # Dismiss Alert
        alert = Alert(driver)
        alert.accept()

        driver.find_element(By.XPATH, "//div[./button[text()='Sign up']]/button[text()='Close']").click()
    ###