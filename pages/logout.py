from selenium.webdriver.common.by import By


class Logout:
    def __new__(cls, *args, **kwargs):
        return super(Logout, cls).__new__(cls, *args, **kwargs)

    def logout(self, driver):
        logout = driver.find_element(By.ID, 'logout2')
        logout.click()
