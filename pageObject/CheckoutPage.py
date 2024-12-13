from selenium.webdriver.common.by import By

from pageObject.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self,driver):
        self.driver = driver
    allphones = (By.XPATH, "//div[@class='card h-100']")
    phonename = (By.XPATH, "div/h4/a")
    addCard = (By.XPATH, "div/button")
    primarybtn = (By.XPATH , "//a[@class='nav-link btn btn-primary']")
    successbtn = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitle(self):
        return self.driver.find_elements(*CheckOutPage.allphones)

    def getPhoneName(self,product):
        return product.find_element(*CheckOutPage.phonename)

    def getAddCard(self, product):
        return product.find_element(*CheckOutPage.addCard)

    def getPrimaryBtn(self):
        return self.driver.find_element(*CheckOutPage.primarybtn)

    def getSuccessBtn(self):
        self.driver.find_element(*CheckOutPage.successbtn).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage