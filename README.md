# GOScraper
Python Web scrapper to collect GO term information from the informatics [website]("http://www.informatics.jax.org/vocab/gene_ontology/")

## Prerequisites 
The runme.py file requires the following installations:
 - Python3 (the code was developed and tested on python3.5.2)
 - Selenium and its WebDriver packages
 - csv package
 - pandas package
 - A browser WebDriver executable (Chrome and FireFox have been tested, runme.py uses Chrome WebDriver). 
   For Windows, this requires the download of ChromeDriver V2.36 ([download link](http://chromedriver.storage.googleapis.com/index.html?path=2.36/)) and added to the PATH variable
 - elements.py file to be in the same directory as the runme.py file that is being run. 

 ## What it collects
 The program can be configured to change what is collect from the website and further specifying GO terms. <b>Currently</b>, It collects ALL GO terms for all 3 categories (Molecular Function, Biological Process and Cellular Component).

 This can be done by changing the following line in the runme.py file:
 ```python
 searchBarInputElem.send_keys(".")
 ```
 where the input to the ```send_keys``` method is changed to the desired GO term of preference. Note: <i>The "." is used to signal ALL GO terms.</i>

 ## How to run
 - Download the repository to your machine
 - Make sure both files ``` runme.py, elements.py``` are in the same directory
 - Run ```runme.py``` using Python; eg ```python3 runme.py```

 ## Output
 A CSV file containing the GO terms are placed in a CSV that is saved to the same directory as ```goTerms.csv```