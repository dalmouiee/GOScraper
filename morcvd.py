#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
import sys, time
import elements
import csv
import pandas as pd

chrome_options = Options()
# remove 'chrome_options.add_argument("--headless")' to allow a browser instance to pop up and observe the program
# chrome_options.add_argument("--headless")
# remove 'chrome_options.add_argument('log-level=3')' to allow for default logging of all info,
# log-levels; 0: info, 1: warning, 2: error, 3: fatal
chrome_options.add_argument('log-level=3')
driver = webdriver.Chrome("/Users/60228808/dev/GOScraper/src/chromedriver", chrome_options=chrome_options)

ignored_exceptions=(StaleElementReferenceException)
wait = WebDriverWait(driver, 20, ignored_exceptions=ignored_exceptions)

def waitForPageToLoadByCssLocator(locator):
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
    except TimeoutException:
        print("Timeout Expection: Could not find the element defined by:" + locator)
        print(sys.exc_info()[0])

def getGoTermDetails():
    waitForPageToLoadByCssLocator(elements.goTermDetailTable)
    goTermDetailTable = driver.find_element(By.CSS_SELECTOR, elements.goTermDetailTable)
    return ((goTermDetailTable.text).split('\n'))

def main():

    print('PROG STATUS(1/10): Opening Page.....................')  
    driver.get(elements.web)
    waitForPageToLoadByCssLocator(elements.disease_btn_id)
    print('PROG STATUS(2/10): Page loaded successfully.....................')

    # 1) Search for all GO terms across all 3 categories using "." as input, then press enter
    print('PROG STATUS(3/10): Loading Disease dropdown page.....................')
    driver.find_element(By.ID, elements.disease_btn_id).click()
    waitForPageToLoadByCssLocator(elements.disease_dropdown_id)

    dropdown_options = driver.find_elements(By.TAG_NAME, "option")
    driver.find_elements()
    print(dropdown_options)

main()