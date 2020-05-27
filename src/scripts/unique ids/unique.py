import pandas as pd
import os
import csv

def check_unique_ids(df, dfRef):
	list = []
	for id1 in df['gene_name']:
		bool = 1
		for id2 in dfRef['Gene symbol']:
			if id1 == id2:
				bool = 0
				break
		if bool == 0:
			pass
		else:
			list.append(id1)
	return list

def write_to_csv(fileName, df, dfRef):
	with open('unique_acore_list_mock.csv', 'w', newline='') as myfile:
		wr = csv.writer(myfile, quoting=csv.QUOTE_ALL,  delimiter = '\n')
		wr.writerow(check_unique_ids(df, dfRef))

def main():
	df1 = pd.read_csv('acore_list.mock.csv')
	df2 = pd.read_csv('acore_list.wt.csv')
	dfRef = pd.read_csv('List of genes.uni.csv')			

	write_to_csv('unique_acore_list_mock.csv', df1, dfRef)
	write_to_csv('unique_acore_list_wt.csv', df2, dfRef)

main()