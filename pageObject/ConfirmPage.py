from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self,driver):
        self.driver = driver

    country = (By.ID, "country")
    country2 = (By.LINK_TEXT, "India")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    sumbit = (By.CSS_SELECTOR, "[type='submit']")
    alert = (By.CLASS_NAME, "alert-success")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getCountry2(self):
        return self.driver.find_element(*ConfirmPage.country2)

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def getSumbit(self):
        return self.driver.find_element(*ConfirmPage.sumbit)

    def getAlert(self):
        return self.driver.find_element(*ConfirmPage.alert)



