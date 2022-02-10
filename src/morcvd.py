"""Script to extract data from the MorCVD website using selenium
This script assumes that there are 2 csv files containing Uniport Acession IDs under a column titled "Entry"
and these 2 files exist in the same directory as this script
"""
from code import interact
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

# Replace this with the path you want to save the files to on your machine
DOWNLOAD_PATH = "/Users/60228808/dev/GOScraper/src/downloads"
# Replace this with the path of the chromiumn driver file on your machine
CHROMIUMN_DRIVER_PATH = "/Users/60228808/dev/GOScraper/src/chromedriver"

logger = logging.basicConfig()

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory": DOWNLOAD_PATH}
chromeOptions.add_experimental_option("prefs", prefs)
chromedriver = CHROMIUMN_DRIVER_PATH

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


def interaction():
    logging.info(
        "Loading Interactions page.....................")
    hidden_btn = driver.find_element(
        By.ID, elements.interact_btn_id)
    driver.execute_script("arguments[0].click();", hidden_btn)
    waitForPageToLoadByCssLocator(
        elements.interact_organism_dropdown_id, By.ID)
    logging.info("Page load success.....................")

    for o in elements.organisms:

        filename, keyword, input_textbox = (
            (
                "uniprot-human-filtered-organism__Homo+sapiens+(Human)+[9606]_.xlsx",
                "human",
                elements.interact_uan_human_input_id
            )
            if o == "HOST_PROTEIN"
            else (
                "uniprot-pathogen-filtered-reviewed_yes.xlsx",
                "pathogen",
                elements.interact_uan_pathogen_input_id)
        )
        organism_interact_dropdown = Select(
            driver.find_element(By.ID, elements.interact_organism_dropdown_id))
        logging.info(
            f"Retrieving {o} Interactions.....................")
        organism_interact_dropdown.select_by_value(o)
        waitForPageToLoadByCssLocator(
            input_textbox, By.ID)

        uan_list = pd.read_excel(filename)["Entry"].tolist()
        for uan in uan_list:
            try:
                prot_uan_input = driver.find_element(
                    By.ID, input_textbox)
                prot_uan_input.send_keys(uan)

                driver.find_element(
                    By.ID, elements.interact_uan_submit_btn_id.replace("*", keyword)).click()
                waitForPageToLoadByCssLocator(
                    elements.interact_results_table_id.replace("*", keyword), By.ID)
                logging.info(
                    f"Downloading {uan} Interactions table.....................")
                driver.find_element(
                    By.ID, elements.interact_download_btn_id.replace("*", keyword)).click()
                logging.info(
                    f"{uan} Interactions table download success.....................")
            except Exception as e:
                logging.error(f"No results found for {uan}! : {e}")
            prot_uan_input = driver.find_element(
                By.ID, input_textbox)
            prot_uan_input.clear()


def inter_detect_multi_meth():
    logging.info(
        "Loading Interaction Detection Multiple Methods dropdown page.....................")
    hidden_btn = driver.find_element(
        By.ID, elements.inter_detect_multi_meth_btn_id)
    driver.execute_script("arguments[0].click();", hidden_btn)
    waitForPageToLoadByCssLocator(
        elements.inter_detect_multi_meth_dropdown_id, By.ID)
    logging.info("Page load success.....................")

    dropdown_options = [option.get_property("value") for option in driver.find_elements(
        By.TAG_NAME, "option")][1:]

    for option in dropdown_options:
        inter_detect_multi_meth_dropdown = Select(driver.find_element(
            By.ID, elements.inter_detect_multi_meth_dropdown_id))
        logging.info(
            f"Retrieving {option} Interaction Detection Multiple Method table.....................")
        inter_detect_multi_meth_dropdown.select_by_value(option)
        driver.find_element(
            By.ID, elements.inter_detect_multi_meth_submit_btn_id).click()
        waitForPageToLoadByCssLocator(
            elements.inter_detect_multi_meth_results_table_id, By.ID)
        logging.info(
            f"{option} Interaction Detection Multiple Method table load success.....................")

        logging.info(
            f"Downloading {option} Interaction Detection Multiple Method table.....................")
        driver.find_element(
            By.ID, elements.inter_detect_multi_meth_download_btn_id).click()
        logging.info(
            f"{option} Interaction Detection Multiple Method table download success.....................")


def inter_detect_meth():
    logging.info(
        "Loading Interaction Detection Method dropdown page.....................")
    hidden_btn = driver.find_element(
        By.ID, elements.inter_detect_meth_btn_id)
    driver.execute_script("arguments[0].click();", hidden_btn)
    waitForPageToLoadByCssLocator(
        elements.inter_detect_meth_dropdown_id, By.ID)
    logging.info("Page load success.....................")

    dropdown_options = [option.get_property("value") for option in driver.find_elements(
        By.TAG_NAME, "option")][1:]

    for option in dropdown_options:
        inter_detect_meth_dropdown = Select(driver.find_element(
            By.ID, elements.inter_detect_meth_dropdown_id))
        logging.info(
            f"Retrieving {option} Interaction Detection Method table.....................")
        inter_detect_meth_dropdown.select_by_value(option)
        driver.find_element(
            By.ID, elements.inter_detect_meth_submit_btn_id).click()
        waitForPageToLoadByCssLocator(
            elements.inter_detect_meth_results_table_id, By.ID)
        logging.info(
            f"{option} Interaction Detection Method table load success.....................")

        logging.info(
            f"Downloading {option} Interaction Detection Method table.....................")
        driver.find_element(
            By.ID, elements.inter_detect_meth_download_btn_id).click()
        logging.info(
            f"{option} Interaction Detection Method table download success.....................")


def gene_onto():
    logging.info(
        "Loading Gene Ontology page.....................")
    driver.find_element(
        By.ID, elements.gene_onto_btn_id).click()
    waitForPageToLoadByCssLocator(
        elements.gene_onto_organism_dropdown_id, By.ID)
    logging.info("Page load success.....................")

    for o in elements.organisms:

        filename, keyword = (
            ("uniprot-human-filtered-organism__Homo+sapiens+(Human)+[9606]_.xlsx",
             "human")
            if o == "HOST_PROTEIN"
            else ("uniprot-pathogen-filtered-reviewed_yes.xlsx", "pathogen")
        )
        organism_gene_onto_dropdown = Select(
            driver.find_element(By.ID, elements.gene_onto_organism_dropdown_id))
        logging.info(
            f"Retrieving {o} Gene Ontology.....................")
        organism_gene_onto_dropdown.select_by_value(o)
        waitForPageToLoadByCssLocator(
            elements.gene_onto_uan_input_id.replace("*", keyword), By.ID)

        uan_list = pd.read_excel(filename)["Entry"].tolist()
        for uan in uan_list:
            try:
                prot_uan_input = driver.find_element(
                    By.ID, elements.gene_onto_uan_input_id.replace("*", keyword))
                prot_uan_input.send_keys(uan)

                driver.find_element(
                    By.ID, elements.gene_onto_uan_submit_btn_id.replace("*", keyword)).click()
                waitForPageToLoadByCssLocator(
                    elements.gene_onto_results_table_id.replace("*", keyword), By.ID)
                logging.info(
                    f"Downloading {uan} Gene Ontology table.....................")
                driver.find_element(
                    By.ID, elements.gene_onto_download_btn_id.replace("*", keyword)).click()
                logging.info(
                    f"{uan} Gene Ontology table download success.....................")
            except Exception as e:
                logging.error(f"No results found for {uan}!")
            prot_uan_input = driver.find_element(
                By.ID, elements.gene_onto_uan_input_id.replace("*", keyword))
            prot_uan_input.clear()


def prot_sped_inter():
    logging.info(
        "Loading Protein Specific Interaction page.....................")
    driver.find_element(
        By.ID, elements.prot_spec_inter_btn_id).click()
    waitForPageToLoadByCssLocator(
        elements.prot_spec_inter_organism_dropdown_id, By.ID)
    logging.info("Page load success.....................")

    for o in ["HOST_PROTEIN"]:

        filename, keyword = (
            ("uniprot-human-filtered-organism__Homo+sapiens+(Human)+[9606]_.xlsx",
             "human")
            if o == "HOST_PROTEIN"
            else ("uniprot-pathogen-filtered-reviewed_yes.xlsx", "pathogen")
        )

        organism_prot_spec_inter_dropdown = Select(
            driver.find_element(By.ID, elements.prot_spec_inter_organism_dropdown_id))
        logging.info(
            f"Retrieving {o} Protein Specific Interation.....................")
        organism_prot_spec_inter_dropdown.select_by_value(o)
        waitForPageToLoadByCssLocator(
            elements.prot_spec_inter_uan_input_id.replace("*", keyword), By.ID)

        uan_list = pd.read_excel(filename)["Entry"].tolist()
        for uan in uan_list:
            try:
                prot_uan_input = driver.find_element(
                    By.ID, elements.prot_spec_inter_uan_input_id.replace("*", keyword))
                prot_uan_input.send_keys(uan)

                driver.find_element(
                    By.ID, elements.prot_spec_inter_uan_submit_btn_id.replace("*", keyword)).click()
                waitForPageToLoadByCssLocator(
                    elements.prot_spec_inter_results_table_id, By.ID)
                logging.info(
                    f"Downloading {uan} Protein Specific Interation table.....................")
                driver.find_element(
                    By.ID, elements.prot_spec_inter_download_btn_id.replace("*", keyword)).click()
                logging.info(
                    f"{uan} Protein Specific Interation table download success.....................")
            except Exception as e:
                logging.error(f"No results found for {uan}!")
            prot_uan_input = driver.find_element(
                By.ID, elements.prot_spec_inter_uan_input_id.replace("*", keyword))
            prot_uan_input.clear()


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
        driver.find_element(
            By.ID, elements.path_spec_inter_download_btn_id).click()
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
        driver.find_element(
            By.ID, elements.disease_download_btn_id).click()
        logging.info(
            f"{option} disease table download success.....................")


def main():
    logging.info("Opening MORCVD Page.....................")
    driver.get(elements.morcvd_url)
    waitForPageToLoadByCssLocator(elements.disease_btn_id, By.ID)
    logging.info("Page load success.....................")

    # Uncomment the functions you wish to run
    disease()
    path_sped_inter()
    # TODO: fix for pathogen pathway
    prot_sped_inter()
    gene_onto()
    inter_detect_meth()
    inter_detect_multi_meth()
    interaction()
    # TODO add common interactors pathway
    # common_interaction()


main()
