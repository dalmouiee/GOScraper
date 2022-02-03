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
chrome_options.add_argument("--headless")
# remove 'chrome_options.add_argument('log-level=3')' to allow for default logging of all info,
# log-levels; 0: info, 1: warning, 2: error, 3: fatal
chrome_options.add_argument('log-level=3')
driver = webdriver.Chrome(chrome_options=chrome_options)

ignored_exceptions=(StaleElementReferenceException)
wait = WebDriverWait(driver, 20, ignored_exceptions=ignored_exceptions)

def waitForPageToLoadByCssLocator(locator):
    try:
        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
    except TimeoutException:
        print("Timeout Expection: Could not find the element defined by:" + locator)
        print(sys.exc_info()[0])

def getGoTermDetails():
    waitForPageToLoadByCssLocator(elements.goTermDetailTable)
    goTermDetailTable = driver.find_element(By.CSS_SELECTOR, elements.goTermDetailTable)
    return ((goTermDetailTable.text).split('\n'))

'''
# Second method which expandable all sub items manually then clicks on each and collects go term details
def findAllExpanables2(rows):
    for row in rows:
        subRows = row.find_elements(By.CSS_SELECTOR, elements.expandSubItemButtonCss)
        subRows[0].click()
        time.sleep(1)
        for subRow in subRows:
            if subRow.find_elements(By.CSS_SELECTOR, elements.categorySubItemsCss) != None:
                findAllExpanables2(subRows)
        break
    return

def expandAllExpanables():
    rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, elements.categorySubItemsCss)))
    if rows != None:
        for row in rows:
            try:
                row.click()
            except:
                pass
        expandAllExpanables()
    return
'''

def main():

    print('PROG STATUS(1/10): Opening Page.....................')  
    driver.get(elements.web)
    waitForPageToLoadByCssLocator(elements.moleFuncClass)
    print('PROG STATUS(2/10): Page loaded successfully.....................')

    '''
    # First, find all LI expandables and click their 'a' to expand them. Keep doing this unitl no more expandables are left
    print('PROG STATUS: Unpacking all gene ontologies, this may take a while (1-15 minutes).....................')
    expandAllExpanables()
    print('PROG STATUS: Unpacking all gene ontologies is done.....................')

    # Second, Go thorugh all sub items and check their 'go term detail'
    '''

    # 1) Search for all GO terms across all 3 categories using "." as input, then press enter
    print('PROG STATUS(3/10): Searching for GO terms.....................')
    searchBarInputElem = driver.find_element_by_css_selector(elements.searchBarInputCss)
    searchBarInputElem.send_keys(".")
    searchBarInputElem.send_keys(Keys.RETURN)

    # 2) Wait for results to load
    print('PROG STATUS(4/10): Waiting for GO terms to load.....................')
    waitForPageToLoadByCssLocator(elements.searchResultsDivsCss)
    print('PROG STATUS(5/10): GO terms loaded successfully.....................')

    # 3) Go thorugh each link one by one and retrieve info from the GO detail pane
    print('PROG STATUS(6/10): Going to save GO term data to DF now (this will take a while).....................')
    
    gTypeLinksElems = driver.find_element_by_css_selector(elements.searchResultsDivsCss)
    count = True
    j = 1
    df = pd.DataFrame(columns=['Term', 'Synonyms', 'Definition', 'Parent Terms', 'Comment', 'Category', 'ID', 'Other IDs'])
    while count:
        tempColumnList = []
        tempValueList = []
        if j != 1:
            gTypeLinksElems =  driver.execute_script(""" return arguments[0].nextElementSibling
                                                     """, gTypeLinksElems)
        if gTypeLinksElems == None:
            count = False
        else:
            link = gTypeLinksElems.find_element_by_css_selector(elements.searchResultLinkCss)
            link.click()
            resultList = getGoTermDetails()
            for i in resultList:
                tempList = i.split(':', 1)
                if len(tempList) == 1:
                    tempValueList[-1] += ' ' + tempList[0]
                else:
                    tempColumnList.append(tempList[0])
                    tempValueList.append(tempList[1])
            tempDf = pd.DataFrame([tempValueList], columns=tempColumnList)
            if j == 1:
                df = tempDf
            else:
                df = df.append(tempDf)
        if j % 10 == 0:
            print(str(j) + ' Go terms have been loaded so far.....................')
        j += 1
    
    print('PROG STATUS(7/10): All GO terms saved to DF successfully!!.....................')
    
    # 4) Save df to csv file
    print('PROG STATUS(8/10): Saving df to csv file now.....................')
    df.to_csv('goTerms.csv', mode='a', index=False)
    print('PROG STATUS(9/10): CSV file produced successfully!!.....................')

    # 5) Close program
    print('PROG STATUS(10/10): Closing page and terminating program now.....................')

main()