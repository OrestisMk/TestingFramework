from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest

from TestData.HomePageData import HomePageData
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSumbission(self, getData):
        log = self.getLogger()

        homepage = HomePage(self.driver)
        log.info("firstname is " + getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheck().click()
        self.selectOptionText(homepage.getGender(),getData["gender"])
        homepage.getSumbit().click()

        message = homepage.getSuccessMessage().text

        assert "success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self,request):
        return request.param