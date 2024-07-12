from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import *
import time

driver = webdriver.Firefox()
driver.install_addon("/Users/gujamarkozashvili/Downloads/pwnfox-1.0.4.xpi",temporary=True)

while True:
    driver.get("https://tbcpay.ge/services/bankebi-sxva-finansuri-momsaxureba/tbc-bank")
    time.sleep(10)
    driver.find_element(By.XPATH,"//input[@type='tel']").send_keys("01001082174")
    driver.find_element(By.ID,"service_input_submit_button").click()
    time.sleep(5)
