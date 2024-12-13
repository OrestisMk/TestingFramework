from selenium.webdriver.common.by import By

from pageObject.CheckoutPage import CheckOutPage


class HomePage:

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class = 'alert alert-success alert-dismissible']")

    def __init__(self,driver):
        self.driver = driver


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click() # with star, it reads the the variable as a tuple
        checkOutPage = CheckOutPage(self.driver)
        return  checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheck(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getSumbit(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)