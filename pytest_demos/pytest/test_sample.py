# in cmd type pip install -U pytest
# to check version of pytest type pytest --version
# For pytest the filename should start or end with test keyword e.g test_aaa.py
# in terminal type pytest test_sample.py will run the file
# in terminal type python -m pytest this commond will run all the files in pytest folders , that files having test keyword in it
# in cmd got to the project folder path > type pytest will run  the test
# in cmd another command path > type pytest -v this means v means verbose , kit will give detailed report of testcase
# if run through class , class name should start with Test , capital T is must
# for html reports in cmd type pip install pytest-html
# in terminal type pytest --html=report.html
# to add reports to another folder type pytest --html=./reports/report1.html
# for allure reports in cmd type pip install allure-pytest
# in pycharm terminal project path type pytest --alluredir=D:\... folder path where report to be stored
# to see that allure report type allure serve D:\.... folder path where allure report is stored

from selenium import webdriver
import time
import pytest


class Testsample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome("D:\python_projects\pytest_demos\drivers\chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("test completed")


    def test_login(self, test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element_by_name("txtUsername").send_keys("Admin")
        driver.find_element_by_name("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        x=driver.title
        assert x == "OrangeHRM"