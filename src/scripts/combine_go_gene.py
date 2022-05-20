"""Script to combine GO and gene information into one matrix
"""
import pandas as pd

df_go = (pd.read_csv("data/Gene.ontology.ID.csv"))
# Filter in only the first 1506 rows from the gene names CSV (Rest is invalid)
df_gene = (pd.read_csv("data/gne.name.csv")).head(1505)

df_results = pd.DataFrame(columns=["gene_name", "go_term"])

# Iterate through both CSVs together
for gene_row, go_row in zip(df_gene.iterrows(), df_go.iterrows()):
    go_final_list = []
    gene_final_list = []
    # Grab only the gene names from the gene CSV
    gene_name_list = list(gene_row[1].dropna().drop("len"))
    # Grab only the go terms from the go term CSV
    go_name_list = list(go_row[1].dropna())
    # Iterate through the filtered gene names and create a copy of each gene name for each go term
    for gene in gene_name_list:
        gene_final_list.extend([gene]*len(go_name_list))
    # Create a copy of each go term for each gene name in order
    go_final_list.extend(go_name_list*len(gene_name_list))
    # Combine this row's gene/go terms into a dataframe 
    df_results = pd.concat([df_results, pd.DataFrame(
        {"go_term": go_final_list, "gene_name": gene_final_list})], ignore_index=True)
# Write the results to a csv
df_results.to_csv("data/gene_go_combine.csv", index=False)
