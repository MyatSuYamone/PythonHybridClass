#19.1.2020 HW 

import csv

with open('names.csv', 'r') as csv_file:
	csv_reader = csv.Dictreader(csv_file)

	with open('new_names.csv','w') as nwe_file;
	fieldnmaes = ['first_name', 'last_name']

	csv_writer = csv.Dictwriter(new_file, filednames = fieldnames, delimiter='\t')

	csv_writer.writeheader()

	for line in csv_reader:
		deel line['email']
		csv_writer.writerow(line)