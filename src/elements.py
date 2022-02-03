#!/usr/bin/python3

# URLs
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

organisms = [
    "HOST_PROTEIN",
    "PATHOGEN_PROTEIN"
]

prot_spec_inter_btn_id = "ContentPlaceHolder_navigation_LinkButton_Protein"
prot_spec_inter_organism_dropdown_id = "MainContent_host_organism_drop"
prot_spec_inter_uan_input_id = "MainContent_*_id_host_textbox"
prot_spec_inter_uan_submit_btn_id = "MainContent_*_host_submit"
prot_spec_inter_results_table_id = "MainContent_protein_pathogen_specific_gridview"
prot_spec_inter_download_btn_id = "MainContent_protein_specific_*_download_data"

gene_onto_btn_id = "ContentPlaceHolder_navigation_LinkButton_Gene"
gene_onto_organism_dropdown_id = "MainContent_gene_ontologies_drop"
gene_onto_uan_input_id = "MainContent_gene_ontologies_*_uniprot_textbox"
gene_onto_uan_submit_btn_id = "MainContent_gene_ontologies_*_uniprot_submit"
gene_onto_results_table_id = "MainContent_gene_ontologies_*_uniprot_gridview"
gene_onto_download_btn_id = "MainContent_gene_ontologies_*_download_data"

inter_detect_meth_btn_id = "ContentPlaceHolder_navigation_LinkButton_Interaction_Methods"
inter_detect_meth_dropdown_id = "MainContent_interaction_detection_method_drop"
inter_detect_meth_submit_btn_id = "MainContent_interaction_detection_method_submit"
inter_detect_meth_results_table_id = "MainContent_interaction_detection_method_gridview"
inter_detect_meth_download_btn_id = "MainContent_interaction_detection_download_data"

inter_detect_multi_meth_btn_id = "ContentPlaceHolder_navigation_LinkButton_Multiple_Methods"
inter_detect_multi_meth_dropdown_id = "MainContent_interaction_detection_multiple_method_drop"
inter_detect_multi_meth_submit_btn_id = "MainContent_interaction_detection_multiple_method_submit"
inter_detect_multi_meth_results_table_id = "MainContent_interaction_multiple_method_gridview"
inter_detect_multi_meth_download_btn_id = "MainContent_interaction_multiple_download_data"

interact_btn_id = "ContentPlaceHolder_navigation_LinkButton_test"
interact_organism_dropdown_id = "MainContent_test_drop"
interact_uan_human_input_id = "MainContent_text_human_textbox"
interact_uan_pathogen_input_id = "MainContent_test_pathogen_textbox"
interact_uan_submit_btn_id = "MainContent_test_*_submit"
interact_results_table_id = "MainContent_test_*_gridview"
interact_download_btn_id = "MainContent_interactors_*_download_data"


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
