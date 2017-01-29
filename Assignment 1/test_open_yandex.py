from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


CHROMEDRIVER_PATH = 'chromedriver'  # It is expected to be either in PATH or in /usr/bin

def get_driver():
    driver = webdriver.Chrome(CHROMEDRIVER_PATH)
    driver.implicitly_wait(30)
    return driver


def test_open_yandex():
    driver = get_driver()
    driver.get('https://yandex.ru/')
    driver.quit()



