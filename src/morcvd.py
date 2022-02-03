from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import sys
import elements
import pandas as pd
import logging
import time

logger = logging.basicConfig()

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory": "/Users/60228808/dev/GOScraper/src/downloads"}
chromeOptions.add_experimental_option("prefs", prefs)
chromedriver = "/Users/60228808/dev/GOScraper/src/chromedriver"

driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)

ignored_exceptions = (StaleElementReferenceException)
wait = WebDriverWait(driver, 20, ignored_exceptions=ignored_exceptions)


def waitForPageToLoadByCssLocator(locator, selector_type):
    try:
        wait.until(EC.presence_of_element_located((selector_type, locator)))
    except TimeoutException:
        logging.error(
            f"Timeout Expection: Could not find the element defined by: + {locator}")
        print(sys.exc_info()[0])


def path_sped_inter():
    logging.info(
        "Loading Pathogen Specific Interaction page.....................")
    driver.find_element(
        By.ID, elements.path_spec_inter_btn_id).click()
    waitForPageToLoadByCssLocator(elements.path_spec_inter_dropdown_id, By.ID)
    logging.info("Page load success.....................")

    dropdown_options = [option.get_property("value") for option in driver.find_elements(
        By.TAG_NAME, "option")][1:]

    for option in dropdown_options:
        path_spec_inter_dropdown = Select(driver.find_element(
            By.ID, elements.path_spec_inter_dropdown_id))
        logging.info(
            f"Retrieving {option} Pathogen Specific Interation table.....................")
        path_spec_inter_dropdown.select_by_value(option)
        driver.find_element(
            By.ID, elements.path_spec_inter_submit_btn_id).click()
        waitForPageToLoadByCssLocator(
            elements.path_spec_inter_results_table_id, By.ID)
        logging.info(
            f"{option} Pathogen Specific Interation table load success.....................")

        logging.info(
            f"Downloading {option} Pathogen Specific Interation table.....................")
        path_spec_inter_dropdown = driver.find_element(
            By.ID, elements.path_spec_inter_download_btn_id).click()
        # waitForPageToLoadByCssLocator(elements.path_spec_inter_dropdown_id, By.ID)
        logging.info(
            f"{option} Pathogen Specific Interation table download success.....................")


def disease():

    logging.info("Loading Disease dropdown page.....................")
    driver.find_element(
        By.ID, elements.disease_btn_id).click()
    waitForPageToLoadByCssLocator(elements.disease_dropdown_id, By.ID)
    logging.info("Page load success.....................")

    dropdown_options = [option.get_property("value") for option in driver.find_elements(
        By.TAG_NAME, "option")][1:]

    for option in dropdown_options:
        disease_dropdown = Select(driver.find_element(
            By.ID, elements.disease_dropdown_id))
        logging.info(f"Retrieving {option} disease table.....................")
        disease_dropdown.select_by_value(option)
        driver.find_element(By.ID, elements.disease_submit_btn_id).click()
        waitForPageToLoadByCssLocator(elements.disease_results_table_id, By.ID)
        logging.info(
            f"{option} disease table load success.....................")

        logging.info(
            f"Downloading {option} disease table.....................")
        disease_dropdown = driver.find_element(
            By.ID, elements.disease_download_btn_id).click()
        # waitForPageToLoadByCssLocator(elements.disease_dropdown_id, By.ID)
        logging.info(
            f"{option} disease table download success.....................")


def main():
    logging.info("Opening MORCVD Page.....................")
    driver.get(elements.morcvd_url)
    waitForPageToLoadByCssLocator(elements.disease_btn_id, By.ID)
    logging.info("Page load success.....................")

    path_sped_inter()


main()
