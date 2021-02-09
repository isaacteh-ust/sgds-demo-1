# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options  

class TestTest():
  def setup_method(self, method):
    chrome_options = Options()  
    chrome_options.add_argument("--headless")  
    self.driver = webdriver.Chrome(chrome_options=chrome_options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test(self):
    self.driver.get("http://127.0.0.1:8080")    
    print('open the site')
    self.driver.save_screenshot("home.png")
    self.driver.find_element_by_xpath('//*[@id="navbarMain"]/div[1]/a[1]').click()
    print('open about')
    self.driver.save_screenshot("about.png")
    self.driver.find_element_by_xpath('//*[@id="navbarMain"]/div[1]/a[2]').click()
    print('open about')
    self.driver.save_screenshot("guides.png")
