#!/usr/bin/python3

#URLs
go_term_url = "http://www.informatics.jax.org/vocab/gene_ontology/"
morcvd_url = "http://morcvd.sblab-nsit.net/About"

# Locator by ID
disease_btn_id = "ContentPlaceHolder_navigation_LinkButton_Disease"
disease_dropdown_id = "MainContent_disease_drop"
disease_submit_btn_id = "MainContent_disease_button"
disease_results_table_id = "MainContent_disease_gridview"
disease_download_btn_id = "MainContent_download_data"

path_spec_inter_btn_id = "ContentPlaceHolder_navigation_LinkButton_Pathogen"
path_spec_inter_dropdown_id = "MainContent_pathogen_specific_drop"
path_spec_inter_submit_btn_id = "MainContent_pathogen_specific_submit"
path_spec_inter_results_table_id = "MainContent_pathogen_specific_gridview"
path_spec_inter_download_btn_id = "MainContent_pathogen_specific_download_data"

# Locators by Class
moleFuncClass = ".jstree-anchor"
firstUserChoiceClass = "enter-form__choose-user"
settingsBtnClass = "user-menu__settings"

# Locators by CSS selector
goTermDetailTable = "#termPaneDetails"
listExpandableCss = "aria-expanded"
categoryCss = "#treeViewDiv ul li a"
categorySubItemsCss = '#treeViewDiv ul li [aria-expanded="false"] a'
checkIfExpandableCss = '[aria-expanded="false"]'
expandSubItemButtonCss = "i"
collectAllSubItemsCss = ".jstree-default a"
searchBarInputCss = "[name='term']"
searchResultsDivsCss = "[id='searchResults'] div"
searchResultLinkCss = "a"