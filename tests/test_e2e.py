from selenium import webdriver
import pytest
from torch.ao.quantization.fx import convert

from pageObject.CheckoutPage import CheckOutPage
from pageObject.ConfirmPage import ConfirmPage
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import sys

sys.stdout.reconfigure(encoding='utf-8')


#@pytest.mark.usefixtures("setup")

class TestOne(BaseClass):
    #trainerudemy @ gmail.com
    def test_e2e(self):

        log = self.getLogger()

        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("getting all core items")
        products = checkOutPage.getCardTitle()

        for product in products:
            phone_name = checkOutPage.getPhoneName(product).text  # Use relative locator
            log.info(phone_name)
            if phone_name == "Blackberry":
                checkOutPage.getAddCard(product).click()

        checkOutPage.getPrimaryBtn().click()
        confirmPage = checkOutPage.getSuccessBtn()
        log.info("Entering country name as ind")
        confirmPage.getCountry().send_keys("ind")
        self.verifylinkPresence("India")
        confirmPage.getCountry2().click()
        confirmPage.getCheckBox().click()
        confirmPage.getSumbit().click()
        successText = confirmPage.getAlert().text
        log.info("Text received from application is {} " + successText.encode('utf-8').decode('utf-8'))

        assert "Success! Thankjj you!" in successText
